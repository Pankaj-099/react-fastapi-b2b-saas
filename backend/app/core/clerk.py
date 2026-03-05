
from clerk_backend_api import Clerk
from app.core.config import settings

Clerk = Clerk(bearer_auth=settings.CLERK_SECRET_KEY)