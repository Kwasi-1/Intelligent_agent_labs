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
    "tls"; -- Add support for secure TLS on c2s/s2s connections
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
    "admin_telnet"; -- Open telnet console interface on localhost port 5582
    
    -- HTTP modules
    "bosh"; -- Enable BOSH clients, aka "Jabber over HTTP"
    "websocket"; -- XMPP over WebSockets
    
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
