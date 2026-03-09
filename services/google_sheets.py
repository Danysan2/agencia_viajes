"""Cliente para Google Sheets API - Versión simplificada para agencia de viajes."""
import uuid
import json
from datetime import datetime
from typing import Optional

# Importaciones opcionales
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False

# Logger opcional
try:
    from loguru import logger
except ImportError:
    class SimpleLogger:
        def info(self, msg): print(f"INFO: {msg}")
        def error(self, msg): print(f"ERROR: {msg}")
        def warning(self, msg): print(f"WARNING: {msg}")
    logger = SimpleLogger()

try:
    from config.settings import SERVICE_ACCOUNT_PATH, GOOGLE_SHEETS_ID, GOOGLE_SCOPES
    from config.constants import SHEET_CLIENTES, SHEET_SESIONES
    from models import Cliente, Sesion
except ImportError:
    logger.warning("⚠️  Configuración no disponible - modo mock")
    SHEET_CLIENTES = "clientes"
    SHEET_SESIONES = "sesiones_chat"


class SheetsClient:
    """Cliente simplificado para Google Sheets - Solo clientes y sesiones."""
    
    def __init__(self):
        """Inicializa el cliente."""
        if not GOOGLE_AVAILABLE:
            logger.warning("⚠️  Google API no disponible - modo mock")
            self.service = None
            return
        
        try:
            import os
            from pathlib import Path
            
            service_account_json = os.getenv('GOOGLE_SERVICE_ACCOUNT_FILE')
            
            if service_account_json and service_account_json.startswith('{'):
                service_account_info = json.loads(service_account_json)
                self.credentials = service_account.Credentials.from_service_account_info(
                    service_account_info,
                    scopes=GOOGLE_SCOPES
                )
            else:
                if not Path(SERVICE_ACCOUNT_PATH).exists():
                    logger.warning("⚠️  Credenciales no encontradas - modo mock")
                    self.service = None
                    return
                
                self.credentials = service_account.Credentials.from_service_account_file(
                    str(SERVICE_ACCOUNT_PATH),
                    scopes=GOOGLE_SCOPES
                )
            
            self.service = build('sheets', 'v4', credentials=self.credentials)
            self.spreadsheet_id = GOOGLE_SHEETS_ID
            logger.info("✅ Google Sheets conectado")
        except Exception as e:
            logger.warning(f"⚠️  Error inicializando Sheets: {e}")
            self.service = None
    
    def _read_range(self, range_name: str):
        """Lee un rango."""
        if not self.service:
            return []
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_name
            ).execute()
            return result.get('values', [])
        except:
            return []
    
    def _append_row(self, sheet_name: str, values):
        """Agrega una fila."""
        if not self.service:
            return True
        try:
            self.service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=f"{sheet_name}!A:Z",
                valueInputOption='RAW',
                body={'values': [values]}
            ).execute()
            return True
        except:
            return False
    
    def _update_row(self, range_name: str, values):
        """Actualiza una fila."""
        if not self.service:
            return True
        try:
            self.service.spreadsheets().values().update(
                spreadsheetId=self.spreadsheet_id,
                range=range_name,
                valueInputOption='RAW',
                body={'values': [values]}
            ).execute()
            return True
        except:
            return False
    
    # === CLIENTES ===
    
    def get_cliente_por_telefono(self, telefono: str) -> Optional:
        """Busca un cliente por teléfono."""
        if not self.service:
            return None
        try:
            rows = self._read_range(f"{SHEET_CLIENTES}!A2:F")
            for row in rows:
                if len(row) > 1 and row[1] == telefono:
                    from models import Cliente
                    return Cliente.from_sheet_row(row)
        except:
            pass
        return None
    
    def crear_cliente(self, telefono: str, nombre: str):
        """Crea un nuevo cliente."""
        try:
            from models import Cliente
            cliente = Cliente(
                id=f"cli_{uuid.uuid4().hex[:8]}",
                telefono=telefono,
                nombre=nombre,
                fecha_registro=datetime.now(),
                total_citas=0
            )
            if self.service:
                self._append_row(SHEET_CLIENTES, cliente.to_sheet_row())
            logger.info(f"Cliente creado: {cliente.id}")
            return cliente
        except:
            return None
    
    def actualizar_cliente(self, cliente, row_index: int) -> bool:
        """Actualiza un cliente."""
        if not self.service:
            return True
        range_name = f"{SHEET_CLIENTES}!A{row_index}:F{row_index}"
        return self._update_row(range_name, cliente.to_sheet_row())
    
    # === SESIONES ===
    
    def get_sesion(self, telefono: str):
        """Obtiene la sesión de un usuario."""
        if not self.service:
            return None
        try:
            rows = self._read_range(f"{SHEET_SESIONES}!A2:E")
            for idx, row in enumerate(rows, start=2):
                if len(row) > 0 and row[0] == telefono:
                    from models import Sesion
                    return Sesion.from_sheet_row(row), idx
        except:
            pass
        return None
    
    def crear_sesion(self, sesion) -> bool:
        """Crea una nueva sesión."""
        if not self.service:
            return True
        return self._append_row(SHEET_SESIONES, sesion.to_sheet_row())
    
    def actualizar_sesion(self, sesion, row_index: int) -> bool:
        """Actualiza una sesión."""
        if not self.service:
            return True
        sesion.ultima_actividad = datetime.now()
        range_name = f"{SHEET_SESIONES}!A{row_index}:E{row_index}"
        return self._update_row(range_name, sesion.to_sheet_row())
    
    def eliminar_sesion(self, telefono: str) -> bool:
        """Elimina una sesión."""
        if not self.service:
            return True
        result = self.get_sesion(telefono)
        if result:
            _, row_index = result
            range_name = f"{SHEET_SESIONES}!A{row_index}:E{row_index}"
            return self._update_row(range_name, ["", "", "", "", ""])
        return False
    
    def test_connection(self) -> bool:
        """Prueba la conexión."""
        if not self.service:
            return False
        try:
            self.service.spreadsheets().get(
                spreadsheetId=self.spreadsheet_id
            ).execute()
            return True
        except:
            return False
