from PyFunceble import *
import status_state

domainChecker = DomainSyntaxChecker()
ipChecker = IPSyntaxChecker()
urlChecker = URLSyntaxChecker()
domainAvailChecker = DomainAvailabilityChecker()

def isActive(status_code):
    return status_code in status_state.ACTIVE

def isInActive(status_code):
    return status_code in status_state.INACTIVE

def isValid(url):
    status = checker.set_subject(url).get_status()
    return status

def isIP(ip):
    status = ipChecker.set_subject(ip).get_status()
    return status.is_valid()

def isDomain(domain):
    status = domainChecker.set_subject(domain).get_status()
    return status.is_valid()

def isDomainActive(domain):
    status = domainAvailChecker.set_subject(domain).get_status()
    return status.is_active()

def isURL(url):
    status = urlChecker.set_subject(url).get_status()
    return status.is_valid()

print(isDomain('medium.com'))