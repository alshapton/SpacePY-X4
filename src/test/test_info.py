
import sys
sys.path.append('../')
import pytest
import spacexpython
from .tutils import *


def test_api():
    api_data = ''
    api_result = alphaOrder(readJSONFile('info/api.json'))
    try:
        api_data = alphaOrder(spacexpython.info.api())
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on info.api")
    assert api_result == api_data


def test_company():
    company_data = ''
    company_result = alphaOrder(readJSONFile('info/company.json'))
    try:
        company_data = alphaOrder(spacexpython.info.company())
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on info.company")
    assert company_data == company_result


def test_clients():
    client_data = ''
    client_result = keyOrder(alphaOrder(
        readJSONFile('info/clients.json')), "Name")
    try:
        client_data = keyOrder(
            alphaOrder(spacexpython.info.clients()), "Name")
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on info.clients")
    assert client_data == client_result

def test_language():
    language_data = ''
    language_result = keyOrder(alphaOrder(
        readJSONFile('info/oneclientmine.json')), "Name")
    # language_result = ""
    try:
        language_data = keyOrder(alphaOrder(
            spacexpython.info.clients(
                '{"Languages":["Python"],'
                ' "Creators":["Andrew Shapton"]}')),"Name")
    except spacexpython.utils.SpaceXReadTimeOut:
        # pytest.xfail("Space/X API Read Timed Out")
        print("Failure on info.clients(Language)")
    print (language_data)
    assert language_data == language_result

def test_apps():
    apps_data = ''
    apps_result=''
    apps_result = keyOrder(alphaOrder(
        readJSONFile('info/apps.json')), "Name")
    try:
        apps_data = keyOrder(
            alphaOrder(spacexpython.info.apps()), "Name")
        # apps_data = spacexpython.info.apps()
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on info.apps")
    print(apps_data)
    assert apps_data == apps_result
    # assert 0 == 1