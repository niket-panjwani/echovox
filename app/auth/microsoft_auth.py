from flask import Flask, session, redirect, url_for, request, Blueprint, session
from app.config import CLIENT_ID, CLIENT_SECRET, TENANT_ID
import msal
import uuid
from flask_cors import cross_origin
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
microsoft_auth_blueprint = Blueprint('microsoft_auth', __name__)

# MSAL configuration
AUTHORITY = f'https://login.microsoftonline.com/{TENANT_ID}'
SCOPES = ['https://graph.microsoft.com/Calendars.ReadWrite']
SESSION_STATE_KEY = 'state'
SESSION_TOKEN_CACHE_KEY = 'token_cache'

# Initialize MSAL Confidential Client Application
cca = msal.ConfidentialClientApplication(
    CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET,
)

def load_cache():
    cache = session.get(SESSION_TOKEN_CACHE_KEY, "")
    if cache:
        deserialized_cache = msal.SerializableTokenCache()
        deserialized_cache.deserialize(cache)
        return deserialized_cache
    return msal.SerializableTokenCache()

def save_cache(cache):
    if cache.has_state_changed:
        session[SESSION_TOKEN_CACHE_KEY] = cache.serialize()

def build_msal_app(cache=None):
    return msal.ConfidentialClientApplication(
        CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET,
        token_cache=cache,
    )

def build_auth_url(authority=None, scopes=None, state=None):
    return cca.get_authorization_request_url(
        scopes or [],
        state=state or str(uuid.uuid4()),
        redirect_uri=url_for('microsoft_auth.authorized', _external=True),
    )

@microsoft_auth_blueprint.route('/login')
@cross_origin()
def login():
    session[SESSION_STATE_KEY] = str(uuid.uuid4())
    auth_url = build_auth_url(scopes=SCOPES, state=session[SESSION_STATE_KEY])
    return redirect(auth_url)

@microsoft_auth_blueprint.route('/callback')  # Callback route
@cross_origin()
def authorized():
    # Ensure the state matches to mitigate CSRF attacks
    if request.args.get('state') != session.get(SESSION_STATE_KEY):
        return redirect(url_for('error'))  # Or some error page

    cache = load_cache()  # Load the cache
    cca = build_msal_app(cache=cache)
    
    # Acquire a token from the authorization code returned
    result = cca.acquire_token_by_authorization_code(
        request.args['code'],
        scopes=SCOPES,
        redirect_uri=url_for('microsoft_auth.authorized', _external=True)
    )
    if "error" in result:
        return f"Login failure: {result.get('error_description')}"
    
    save_cache(cca.token_cache)
    session['user'] = result.get('id_token_claims')

    # Successful authentication, redirect to a logged-in page
    return redirect(url_for('index'))  # Or wherever you want

def is_user_logged_in():
    print(session)
    return 'user' in session