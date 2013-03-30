# -*- coding: utf-8 -*-
from nose.tools import *
from libpynexmo.nexmomessage import NexmoMessage
from phonenumbers import PhoneNumber, NumberFormat, phonenumberutil

p_loc = '04132445678'
p_int = '8864132445678'

def setup():
    global p_loc
    global p_int

def teardown():
    pass

@with_setup(setup, teardown)
def test_phonenumber():
    p = phonenumberutil.parse(p_loc, 'TW')
    i = phonenumberutil.parse(p_int, 'TW')
    print phonenumberutil.is_number_match(p, i)
    assert_equal(phonenumberutil.MatchType.EXACT_MATCH, phonenumberutil.is_number_match(p, i))

