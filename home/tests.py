from django.test import TestCase

# Create your tests here.


x="{'messaging_product': 'whatsapp', 'recipient_type': 'individual', 'to': '201282050382'," \
  " 'type': 'interactive', " \
  "'interactive': {'type': 'list', " \
  "'body': {'text': 'appoiment \n Price 150.00 \n app'}, " \
  "'action': {'button': 'Dates', " \
  "'sections': [{'title': 'Schedules'," \
  " 'rows': [" \
  "{'id': 753, 'title': 'Monday', 'description': datetime.date(2023, 11, 13)}, " \
  "{'id': 754, 'title': 'Tuesday', 'description': datetime.date(2023, 11, 14)}, " \
  "{'id': 755, 'title': 'Wendensady', 'description': datetime.date(2023, 11, 15)}, " \
  "{'id': 756, 'title': 'Thursday', 'description': datetime.date(2023, 11, 16)}," \
  " {'id': 759, 'title': 'Sunday', 'description': datetime.date(2023, 11, 19)}" \
  "]" \
  "}]" \
  "}}}"