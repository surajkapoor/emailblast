from app import app
from flask import render_template
from config import *
from extensions import mail, Message
from email_template import email_template, email_template2
from models import Companies
import csv
import pdb
from utils import ROLE_MAP, DB_FIELDS, EMAIL_FIELDS
from random import shuffle
import re

QUERY_CACHE = {}


def __build_CACHE__():
	for role in DB_FIELDS:
		value = session.query(Companies).filter_by(**{role : True})
		QUERY_CACHE[role] = value
	return	


def build_dictionary(recommendations):
	email_recommendations = {}
	for rec, field in zip(EMAIL_FIELDS, recommendations):
		email_recommendations[rec] = field	
	return email_recommendations			


def roles_to_recommendations(row):
	roles = [r.strip() for r in row.split(",")]
	recommendations = []
	NAMECHECK = {}
	for role in roles:
		if role in ROLE_MAP:
			for orm in QUERY_CACHE[ROLE_MAP[role]]:

				if orm.linkedin_desc_1 != "(no description available)" and orm.profile_pic_1 != "/static/generic.jpg" and orm.person_name_1 not in NAMECHECK:
					recommendations.append([orm.company_name, orm.person_name_1, orm.linkedin_1, orm.profile_pic_1, orm.linkedin_desc_1, role])
					NAMECHECK[orm.person_name_1] = True

				if orm.linkedin_desc_2 != "(no description available)" and orm.linkedin_desc_2 != None and orm.profile_pic_2 != "/static/generic.jpg" and orm.profile_pic_2 != None and orm.person_name_2 not in NAMECHECK:
					recommendations.append([orm.company_name, orm.person_name_2, orm.linkedin_2, orm.profile_pic_2, orm.linkedin_desc_2, role])	
					NAMECHECK[orm.person_name_2] = True

				if orm.linkedin_desc_3 != "(no description available)" and orm.linkedin_desc_3 != None and orm.profile_pic_3 != "/static/generic.jpg" and orm.profile_pic_3 != None and orm.person_name_3 not in NAMECHECK:
					recommendations.append([orm.company_name, orm.person_name_3, orm.linkedin_3, orm.profile_pic_3, orm.linkedin_desc_3, role])	
					NAMECHECK[orm.person_name_3] = True

	shuffle(recommendations)		
	return build_dictionary(recommendations[:9])



@app.route("/__execute_mailing__/")
def __execute_mailing__():
	__build_CACHE__()
	with open('/Users/surajkapoor/Desktop/hacklist.csv', "rU") as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			first_name, email, interested_roles = row[0], row[1].strip(), roles_to_recommendations(row[2])
			if len(interested_roles) < 9:
				pass
			else:	
				msg = Message(subject="hello", sender="Suraj Kapoor", recipients=[email], html=email_template() + email_template2(first_name, interested_roles))
				mail.send(msg)
	return "DONE"		



