import datetime

from flask_restful import Resource, reqparse

from tools import Settings

post_settings_parser = reqparse.RequestParser()
post_settings_parser.add_argument("pin", type=str, required=False)
post_settings_parser.add_argument("session_duration", type=float, required=False)
post_settings_parser.add_argument("amount_of_questions", type=int, required=False)
post_settings_parser.add_argument("time_period", type=float, required=False)
post_settings_parser.add_argument("from_time", type=str, required=False)
post_settings_parser.add_argument("to_time", type=str, required=False)
post_settings_parser.add_argument("week_days", type=int, required=False, action="append")
post_settings_parser.add_argument("webhook", type=str, required=False)



class SettingsResource(Resource):
    def get(self):
        current_settings = Settings().copy()
        return current_settings, 200

    def post(self):
        current_settings = Settings()
        args = {k: v for k, v in post_settings_parser.parse_args().items() if v is not None and k in current_settings}

        if "pin" in args.keys():
            args["pin"] = int(args["pin"])

        if "time_period" in args:
            args["time_period"] = datetime.timedelta(seconds=args["time_period"])

        if "from_time" in args:
            args["from_time"] = datetime.time.fromisoformat(args["from_time"])

        if "to_time" in args:
            args["to_time"] = datetime.time.fromisoformat(args["to_time"])

        current_settings.update(args)
        current_settings.update_settings()
        return 200
