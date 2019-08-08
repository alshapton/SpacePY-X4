import requests
import urldata
import utils

def company(timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.main_info
    return utils.makeRequest(requestUrl,timeOut)

def api(timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.main_api
    return utils.makeRequest(requestUrl,timeOut)
