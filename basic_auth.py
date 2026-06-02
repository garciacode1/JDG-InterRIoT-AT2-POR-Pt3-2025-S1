import base64
import binascii

from starlette.authentication import (
    AuthenticationBackend,
    AuthenticationError,
    AuthCredentials,
    SimpleUser
)


class BasicAuth(AuthenticationBackend):

    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return None

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()

            if scheme.lower() != "basic":
                raise AuthenticationError("Invalid authentication scheme")

            decoded = base64.b64decode(credentials).decode("ascii")

        except (ValueError, UnicodeDecodeError, binascii.Error):
            raise AuthenticationError("Invalid credentials format")

        username, _, password = decoded.partition(":")

        # Simple hardcoded check for this assessment
        if username not in ["alice", "bob"] or password != "password":
            raise AuthenticationError("Invalid credentials")

        return AuthCredentials(["authenticated"]), SimpleUser(username)
