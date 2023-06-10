from typing import Any
from DtoLib.dto_field import DtoField
from DtoLib.exceptions import DtoValueInvalid


class AbstractDto():

    def __init__(self, args: dict[str, Any]) -> None:
        self.dto_fields = self.__get_dto_fields()
        self.__set_dto_fields_values(args)

    def __get_dto_fields(self) -> dict[str, DtoField]:
        dto_fields = {}
        for attribute_name in self.__dir__():
            attribute = getattr(self, attribute_name)
            if isinstance(attribute, DtoField):
                dto_fields[attribute_name] = attribute
        return dto_fields

    def __set_dto_fields_values(self, values: dict[str, Any]):
        for key, value in values.items():
            attribute = self.dto_fields.get(key)
            if attribute:            
                    attribute.set_value(value)

    def dict(self) -> dict[str,Any]:
        data_dict = {}
        for key,dto in self.dto_fields.items():
            data_dict[key] = dto.value if dto.is_valid else DtoValueInvalid(dto.help)
        return {k:v for k,v in  data_dict.items() if v is not None}