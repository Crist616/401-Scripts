description = [[
Gathers information about the web server by making a simple HTTP request and 
parsing the 'Server' header in the response.
]]

-- Importing necessary libraries
local http = require "http"
local stdnse = require "stdnse"
local nmap = require "nmap"
local string = require "string"

-- Defining the script
author = "Crist"
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"
categories = {"default", "discovery", "safe"}

-- The action function is called for each host/port pair
action = function(host, port)
    -- Making sure the port is open
    if nmap.is_port_open(host, port) then
        -- Perform an HTTP request
        local response = http.get(host, port, "/")
        if response then
            -- Attempt to parse the 'Server' header
            local server_header = response.header["server"]
            if server_header then
                return "Web server: " .. server_header
            else
                return "Server header not found."
            end
        else
            return "HTTP request failed."
        end
    else
        return "Port is not open."
    end
end