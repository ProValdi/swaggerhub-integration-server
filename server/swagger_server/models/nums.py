# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Nums(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, num1: float=None, num2: float=None, operation: str=None):  # noqa: E501
        """Nums - a model defined in Swagger

        :param num1: The num1 of this Nums.  # noqa: E501
        :type num1: float
        :param num2: The num2 of this Nums.  # noqa: E501
        :type num2: float
        :param operation: The operation of this Nums.  # noqa: E501
        :type operation: str
        """
        self.swagger_types = {
            'num1': float,
            'num2': float,
            'operation': str
        }

        self.attribute_map = {
            'num1': 'num1',
            'num2': 'num2',
            'operation': 'operation'
        }
        self._num1 = num1
        self._num2 = num2
        self._operation = operation

    @classmethod
    def from_dict(cls, dikt) -> 'Nums':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Nums of this Nums.  # noqa: E501
        :rtype: Nums
        """
        return util.deserialize_model(dikt, cls)

    @property
    def num1(self) -> float:
        """Gets the num1 of this Nums.


        :return: The num1 of this Nums.
        :rtype: float
        """
        return self._num1

    @num1.setter
    def num1(self, num1: float):
        """Sets the num1 of this Nums.


        :param num1: The num1 of this Nums.
        :type num1: float
        """

        self._num1 = num1

    @property
    def num2(self) -> float:
        """Gets the num2 of this Nums.


        :return: The num2 of this Nums.
        :rtype: float
        """
        return self._num2

    @num2.setter
    def num2(self, num2: float):
        """Sets the num2 of this Nums.


        :param num2: The num2 of this Nums.
        :type num2: float
        """

        self._num2 = num2

    @property
    def operation(self) -> str:
        """Gets the operation of this Nums.

        Types of operations  # noqa: E501

        :return: The operation of this Nums.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation: str):
        """Sets the operation of this Nums.

        Types of operations  # noqa: E501

        :param operation: The operation of this Nums.
        :type operation: str
        """
        allowed_values = ["+", "-", "*"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"
                .format(operation, allowed_values)
            )

        self._operation = operation
