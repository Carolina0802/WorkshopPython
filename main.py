from app.main.infrastructure.providers import configure_dependencies
from app.main.domain.helpers.mapper_config_helper import MapperConfigHelpers

def main():
    
    # Configurar dependencias y obtener el servicio
    service = configure_dependencies(MapperConfigHelpers.FILE_PATH)
    
    # Usar el servicio para obtener y mostrar los datos
    data = service.get_data()
    for record in data:
        print(record.name, record.age, record.balance, record.is_active, record.join_date)

if __name__ == '__main__':
    main()
