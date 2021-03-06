# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Trade(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, connection_id=None, instrument_id=None, created_on=None, updated_on=None, price=None, state=None, amount=None, direction=None, profit_loss_pips=None, profit_loss=None, close_strategy=None):
        """
        Trade - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'connection_id': 'str',
            'instrument_id': 'str',
            'created_on': 'int',
            'updated_on': 'int',
            'price': 'float',
            'state': 'str',
            'amount': 'float',
            'direction': 'str',
            'profit_loss_pips': 'float',
            'profit_loss': 'float',
            'close_strategy': 'CloseStrategy'
        }

        self.attribute_map = {
            'id': 'id',
            'connection_id': 'connectionId',
            'instrument_id': 'instrumentId',
            'created_on': 'createdOn',
            'updated_on': 'updatedOn',
            'price': 'price',
            'state': 'state',
            'amount': 'amount',
            'direction': 'direction',
            'profit_loss_pips': 'profitLossPips',
            'profit_loss': 'profitLoss',
            'close_strategy': 'closeStrategy'
        }

        self._id = id
        self._connection_id = connection_id
        self._instrument_id = instrument_id
        self._created_on = created_on
        self._updated_on = updated_on
        self._price = price
        self._state = state
        self._amount = amount
        self._direction = direction
        self._profit_loss_pips = profit_loss_pips
        self._profit_loss = profit_loss
        self._close_strategy = close_strategy


    @property
    def id(self):
        """
        Gets the id of this Trade.


        :return: The id of this Trade.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Trade.


        :param id: The id of this Trade.
        :type: str
        """

        self._id = id

    @property
    def connection_id(self):
        """
        Gets the connection_id of this Trade.


        :return: The connection_id of this Trade.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this Trade.


        :param connection_id: The connection_id of this Trade.
        :type: str
        """

        self._connection_id = connection_id

    @property
    def instrument_id(self):
        """
        Gets the instrument_id of this Trade.


        :return: The instrument_id of this Trade.
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """
        Sets the instrument_id of this Trade.


        :param instrument_id: The instrument_id of this Trade.
        :type: str
        """

        self._instrument_id = instrument_id

    @property
    def created_on(self):
        """
        Gets the created_on of this Trade.


        :return: The created_on of this Trade.
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """
        Sets the created_on of this Trade.


        :param created_on: The created_on of this Trade.
        :type: int
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """
        Gets the updated_on of this Trade.


        :return: The updated_on of this Trade.
        :rtype: int
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """
        Sets the updated_on of this Trade.


        :param updated_on: The updated_on of this Trade.
        :type: int
        """

        self._updated_on = updated_on

    @property
    def price(self):
        """
        Gets the price of this Trade.


        :return: The price of this Trade.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this Trade.


        :param price: The price of this Trade.
        :type: float
        """

        self._price = price

    @property
    def state(self):
        """
        Gets the state of this Trade.


        :return: The state of this Trade.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Trade.


        :param state: The state of this Trade.
        :type: str
        """
        allowed_values = ["OPEN", "CLOSED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def amount(self):
        """
        Gets the amount of this Trade.


        :return: The amount of this Trade.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Trade.


        :param amount: The amount of this Trade.
        :type: float
        """

        self._amount = amount

    @property
    def direction(self):
        """
        Gets the direction of this Trade.


        :return: The direction of this Trade.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this Trade.


        :param direction: The direction of this Trade.
        :type: str
        """
        allowed_values = ["SHORT", "LONG"]
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def profit_loss_pips(self):
        """
        Gets the profit_loss_pips of this Trade.


        :return: The profit_loss_pips of this Trade.
        :rtype: float
        """
        return self._profit_loss_pips

    @profit_loss_pips.setter
    def profit_loss_pips(self, profit_loss_pips):
        """
        Sets the profit_loss_pips of this Trade.


        :param profit_loss_pips: The profit_loss_pips of this Trade.
        :type: float
        """

        self._profit_loss_pips = profit_loss_pips

    @property
    def profit_loss(self):
        """
        Gets the profit_loss of this Trade.


        :return: The profit_loss of this Trade.
        :rtype: float
        """
        return self._profit_loss

    @profit_loss.setter
    def profit_loss(self, profit_loss):
        """
        Sets the profit_loss of this Trade.


        :param profit_loss: The profit_loss of this Trade.
        :type: float
        """

        self._profit_loss = profit_loss

    @property
    def close_strategy(self):
        """
        Gets the close_strategy of this Trade.


        :return: The close_strategy of this Trade.
        :rtype: CloseStrategy
        """
        return self._close_strategy

    @close_strategy.setter
    def close_strategy(self, close_strategy):
        """
        Sets the close_strategy of this Trade.


        :param close_strategy: The close_strategy of this Trade.
        :type: CloseStrategy
        """

        self._close_strategy = close_strategy

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
