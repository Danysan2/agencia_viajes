"""Constantes del negocio."""

# Información de la agencia
AGENCIA_NOMBRE = "Viajes Colombia Tours"
AGENCIA_TELEFONO = "+57 300 000 0000"
AGENCIA_SEDE = "Bogotá, Colombia"
AGENCIA_HORARIO = "Lunes a sábado, 8am – 6pm"

# Destinos disponibles
DESTINOS = {
    "bogota": {
        "id": "dest_bogota",
        "nombre": "Bogotá",
        "emoji": "🏛️",
        "descripcion": "La capital colombiana, ciudad de historia y cultura"
    },
    "medellin": {
        "id": "dest_medellin",
        "nombre": "Medellín",
        "emoji": "🌸",
        "descripcion": "La ciudad de la eterna primavera"
    },
    "cartagena": {
        "id": "dest_cartagena",
        "nombre": "Cartagena",
        "emoji": "🏖️",
        "descripcion": "La joya del Caribe colombiano"
    },
    "arauca": {
        "id": "dest_arauca",
        "nombre": "Arauca",
        "emoji": "🌾",
        "descripcion": "Tierra de llanuras y tradición"
    }
}

# Hoteles por destino
HOTELES = {
    "cartagena": [
        {
            "id": "hotel_muralla_real",
            "nombre": "Hotel Muralla Real",
            "destino": "Cartagena",
            "precio_noche": 350000,
            "incluye": [
                "Desayuno buffet para 2 personas",
                "Habitación doble con vista al mar",
                "Acceso a piscina y spa",
                "Wi-Fi de alta velocidad",
                "Traslado aeropuerto - hotel"
            ],
            "imagen": "hotel_muralla_real.png"
        },
        {
            "id": "hotel_caribe_boutique",
            "nombre": "Hotel Caribe Boutique",
            "destino": "Cartagena",
            "precio_noche": 280000,
            "incluye": [
                "Desayuno continental",
                "Habitación estándar",
                "Piscina",
                "Wi-Fi gratuito"
            ],
            "imagen": "hotel_caribe_boutique.png"
        },
        {
            "id": "hotel_playa_dorada",
            "nombre": "Hotel Playa Dorada",
            "destino": "Cartagena",
            "precio_noche": 420000,
            "incluye": [
                "Todo incluido",
                "Habitación frente al mar",
                "3 restaurantes",
                "Bar en la playa",
                "Actividades acuáticas"
            ],
            "imagen": "hotel_playa_dorada.png"
        }
    ],
    "medellin": [
        {
            "id": "hotel_poblado_plaza",
            "nombre": "Hotel Poblado Plaza",
            "destino": "Medellín",
            "precio_noche": 250000,
            "incluye": [
                "Desayuno buffet",
                "Habitación ejecutiva",
                "Gimnasio y spa",
                "Wi-Fi de alta velocidad",
                "Parqueadero gratuito"
            ],
            "imagen": "hotel_poblado_plaza.png"
        },
        {
            "id": "hotel_laureles_suites",
            "nombre": "Hotel Laureles Suites",
            "destino": "Medellín",
            "precio_noche": 180000,
            "incluye": [
                "Desayuno americano",
                "Suite con cocina",
                "Piscina",
                "Wi-Fi gratuito"
            ],
            "imagen": "hotel_laureles_suites.png"
        }
    ],
    "bogota": [
        {
            "id": "hotel_zona_t",
            "nombre": "Hotel Zona T",
            "destino": "Bogotá",
            "precio_noche": 220000,
            "incluye": [
                "Desayuno buffet",
                "Habitación deluxe",
                "Gimnasio 24/7",
                "Wi-Fi de alta velocidad",
                "Centro de negocios"
            ],
            "imagen": "hotel_zona_t.png"
        },
        {
            "id": "hotel_candelaria_colonial",
            "nombre": "Hotel Candelaria Colonial",
            "destino": "Bogotá",
            "precio_noche": 150000,
            "incluye": [
                "Desayuno típico",
                "Habitación colonial",
                "Tour por La Candelaria",
                "Wi-Fi gratuito"
            ],
            "imagen": "hotel_candelaria_colonial.png"
        }
    ],
    "arauca": [
        {
            "id": "hotel_llanos_plaza",
            "nombre": "Hotel Llanos Plaza",
            "destino": "Arauca",
            "precio_noche": 120000,
            "incluye": [
                "Desayuno llanero",
                "Habitación estándar",
                "Piscina",
                "Wi-Fi gratuito",
                "Tour por los llanos"
            ],
            "imagen": "hotel_llanos_plaza.png"
        }
    ]
}

# Promociones especiales
PROMOCIONES = [
    {
        "id": "promo_cartagena_express",
        "nombre": "Cartagena Express",
        "destino": "Cartagena",
        "noches": 3,
        "personas": 2,
        "precio_antes": 1200000,
        "precio_ahora": 899000,
        "incluye": "Hotel + Desayuno + Traslados",
        "valido_hasta": "31 de marzo de 2026"
    },
    {
        "id": "promo_medellin_city",
        "nombre": "Medellín City Tour",
        "destino": "Medellín",
        "noches": 2,
        "personas": 2,
        "precio_antes": 900000,
        "precio_ahora": 650000,
        "incluye": "Hotel + City Tour + Cena romántica",
        "valido_hasta": "31 de marzo de 2026"
    }
]

# Estados conversacionales
ESTADO_INICIO = "inicio"
ESTADO_MENU_PRINCIPAL = "menu_principal"
ESTADO_VER_DESTINOS = "ver_destinos"
ESTADO_VER_HOTELES = "ver_hoteles"
ESTADO_VER_DETALLE_HOTEL = "ver_detalle_hotel"
ESTADO_VER_PROMOCIONES = "ver_promociones"
ESTADO_CONTACTO_HUMANO = "contacto_humano"

# Nombres de sheets (mantener compatibilidad)
SHEET_CLIENTES = "clientes"
SHEET_SESIONES = "sesiones_chat"
