from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    user: str = "iauser"
    password: str = "secret"
    host: str = "localhost"
    port: str = "5432"
    database: str = "iadb"

    @property
    def connection_string(self) -> str:
        return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

db_config = DatabaseConfig() 