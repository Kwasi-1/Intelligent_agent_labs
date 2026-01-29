-- Prosody XMPP Server Configuration for Lab Environment
-- Disaster Response & Relief Coordination System

-- Server settings
admins = { "admin@localhost" }

-- Process management
pidfile = "/var/run/prosody/prosody.pid"
daemonize = true

-- Enable required modules
modules_enabled = {
    -- Generally required
    "roster"; -- Allow users to have a roster
    "saslauth"; -- Authentication
    "dialback"; -- s2s dialback support
    "disco"; -- Service discovery
    
    -- Not essential, but recommended
    "carbons"; -- Keep multiple clients in sync
    "pep"; -- Enables users to publish their avatar, mood, activity, playing music and more
    "private"; -- Private XML storage
    "blocklist"; -- Allow users to block communications with other users
    "vcard4"; -- User profiles (stored in PEP)
    "vcard_legacy"; -- Conversion between legacy vCard and PEP Avatar, vcard
    
    -- Admin interfaces
    "admin_adhoc"; -- Allows administration via an XMPP client that supports ad-hoc commands

    -- Other specific functionality
    "ping"; -- Replies to XMPP pings with pongs
    "register"; -- Allow users to register on this server using a client and change passwords
    "time"; -- Let others know the time here on this server
    "uptime"; -- Report how long server has been running
    "version"; -- Replies to server version requests
}

-- Disable modules
modules_disabled = {
    -- "offline"; -- Store offline messages
    -- "c2s"; -- Handle client connections
    -- "s2s"; -- Handle server-to-server connections
}

-- Allow registration
allow_registration = true

-- For local development - allow all connections
c2s_require_encryption = false
s2s_require_encryption = false
s2s_secure_auth = false

-- Allow insecure connections for local testing
allow_unencrypted_plain_auth = true

ssl = {
    key = "/var/lib/prosody/localhost.key";
    certificate = "/var/lib/prosody/localhost.crt";
    protocol = "tlsv1";
    ciphers = "ALL";
}

-- Logging configuration
log = {
    info = "/var/log/prosody/prosody.log";
    error = "/var/log/prosody/prosody.err";
}

-- Virtual hosts
VirtualHost "localhost"
    authentication = "internal_plain"

-- Component for agent communication (optional)
Component "agents.localhost"
    component_secret = "agent_secret_123"
    ssl = {
        key = "/var/lib/prosody/agents.localhost.key";
        certificate = "/var/lib/prosody/agents.localhost.crt";
        protocol = "tlsv1";
        ciphers = "ALL";
    }

-- Limit ports to avoid conflicts in Codespaces
c2s_ports = { 5222 }
s2s_ports = {}
legacy_ssl_ports = {}
http_ports = {}
https_ports = {}
component_ports = {}
