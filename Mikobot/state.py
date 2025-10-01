# https://github.com/Mythic-botz/YaeMiko
# https://github.com/Team-ProjectCodeX

# <============================================== IMPORTS =========================================================>
from aiohttp import ClientSession
from httpx import AsyncClient, Timeout
from Python_ARQ import ARQ

# <=============================================== SETUP ========================================================>
# HTTPx Async Client
state = AsyncClient(
    http2=True,
    verify=False,
    headers={
        "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/107.0.1418.42",
    },
    timeout=Timeout(20),
)

# <=============================================== ARQ SETUP ========================================================>
ARQ_API_KEY = "VOIKGQ-UWUBUP-OAFSHG-UWUOJF-ARQ"  # GET API KEY FROM @ARQRobot
ARQ_API_URL = "arq.hamker.dev"

async def get_session():
    """Create and return a new aiohttp ClientSession."""
    return ClientSession()

async def close_session(session):
    """Close the given aiohttp ClientSession."""
    if session and not session.closed:
        await session.close()

# Initialize ARQ with a new session
async def init_arq():
    session = await get_session()
    return ARQ(ARQ_API_URL, ARQ_API_KEY, session)

arq = None  # Will be initialized in main.py

# <=============================================== CLEANUP ========================================================>
async def cleanup():
    """Close the httpx AsyncClient and any open aiohttp sessions."""
    if state and not state.is_closed:
        await state.aclose()
    if arq and arq.session and not arq.session.closed:
        await arq.session.close()

# <===================================================== END ==================================================>