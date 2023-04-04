import json
import tomllib  # requires Python 3.11+
from typing import Any

from pydantic import BaseModel, conint
import yaml  # from PyYAML


def config_from_json() -> dict[str, Any | None]:
    with open("demo.json", encoding="utf-8") as json_file:
        return json.load(json_file)


def config_from_yaml() -> dict[str, Any | None]:
    with open("demo.yaml", encoding="utf-8") as yaml_file:
        return yaml.load(yaml_file, yaml.FullLoader)


def config_from_toml() -> dict[str, Any | None]:
    with open("demo.toml", "rb") as toml_file:
        return tomllib.load(toml_file)


class Customer(BaseModel):
    name: str
    born: conint(ge=1900)  # "constraint int, greater or equal"


class Config(BaseModel):
    color: str
    customers: list[Customer]


if __name__ == '__main__':
    config_map = config_from_json()
    print(config_map["customers"][0]["name"])  # John Smith

    for config_map in [config_from_json(), config_from_yaml(), config_from_toml()]:
        print(config_map)
        print(config_map["customers"][0]["name"])

        # Validate and parse into to data class
        config = Config(**config_map)
        print(config)
        print(config.customers[0].name)
