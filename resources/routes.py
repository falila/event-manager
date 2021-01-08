from resources.auth import SignupApi, LoginApi
from resources.event import EventApi, EventsApi
from resources.reset_password import ForgotPassword, ResetPassword


def initialize_routes(api):
    api.add_resource(EventApi, "/api/event/<id>")
    api.add_resource(EventsApi, "/api/events")
    api.add_resource(SignupApi, "/api/auth/signup")
    api.add_resource(LoginApi, "/api/auth/login")
    api.add_resource(ForgotPassword, "/api/auth/forgot")
    api.add_resource(ResetPassword, "/api/auth/reset")
