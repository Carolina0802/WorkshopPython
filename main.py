from app.main.infrastructure.di.dependency_injection import inject_dependencies

def main():
    csv_reader_service = inject_dependencies()
    data = csv_reader_service.read_data()
    csv_reader_service.print_data(data)

if __name__ == '__main__':
    main()
