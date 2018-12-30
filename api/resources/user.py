from flask import jsonify, g

from api.resources.base import AuthResource


class CheckIn(AuthResource):
    def get(self, year, month, day):
        return jsonify(g.user.get_checkin_info(year, month))

    def post(self, year, month, day):
        if g.user.checkin(year, month, day):
            return 201
        else:
            return 403


class ReviewHistory(AuthResource):
    def get(self, num_of_days):
        return jsonify(g.user.get_least_history(num_of_days))

