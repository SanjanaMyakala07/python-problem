from abc import ABC, abstractmethod

# Abstract Base Class for the ETL Process
class ETLProcess(ABC):
    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def load(self, data):
        pass

    def run(self):
        data = self.extract()
        transformed_data = self.transform(data)
        self.load(transformed_data)

# Concrete Implementation of the ETLProcess
class SalesETL(ETLProcess):
    def extract(self):
        # Example data extraction
        data = [
            {"id": 1, "name": "Product A", "sales": 100},
            {"id": 2, "name": "Product B", "sales": 200}
        ]
        return data

    def transform(self, data):
        # Example transformation: Normalize sales figures
        for record in data:
            record["sales"] = record["sales"] / 100
        return data

    def load(self, data):
        # Example loading: Print the data to the console
        for record in data:
            print(f"ID: {record['id']}, Name: {record['name']}, Sales: {record['sales']}")

if __name__ == "__main__":
    etl = SalesETL()
    etl.run()