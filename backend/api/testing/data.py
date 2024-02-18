import hashlib

from api.admin.appointment import AppointmentBase
from api.admin.appointment import create_appointment, update_appointment, get_appointment
from api.admin.contact import ContactBase
from api.admin.contact import create_contact, update_contact, get_contact
from api.admin.facility import FacilityBase
from api.admin.facility import create_facility, update_facility, get_facility
from api.admin.medication import MedicationBase
from api.admin.medication import create_medication, update_medication, get_medication
from api.admin.question import QuestionBase
from api.admin.question import create_question, update_question, get_question
from api.admin.response import ResponseBase
from api.admin.response import create_response, update_response, get_response
from api.admin.schedule import ScheduleBase
from api.admin.schedule import create_schedule, update_schedule, get_schedule
from api.admin.session import SessionBase
from api.admin.session import create_session, update_session, get_session
from api.admin.survey import SurveyBase
from api.admin.survey import create_survey, update_survey, get_survey
from api.admin.task import TaskBase
from api.admin.task import create_task, update_task, get_task
from api.admin.users import UserBase
from api.admin.users import create_user, update_user, get_user


# Some UUIDs


# 2d13644a-a20b-41f0-88bb-d74efe3cdb58
# 022ab58b-c8d3-41c8-86d4-f7f805e22e71
# f4c3b5b7-eb87-4b32-8787-5b5df904547f
# 6afbd074-731c-4184-92d1-0ba950ec6e83
# f548ada4-d23e-4eb5-bf00-bf929ecbe509
# 71e85b83-b21d-4a64-bbd5-b4ce0463c135
# d6a0ca3c-a226-4974-88d3-aa42a8e6672a
# d14faf56-954f-4e5a-b00b-ccd0d6fe0160
# d3c787c4-866c-46fd-b3a2-3f43b7309269
# a12cebfd-743d-40e0-a82b-bf20ccdf39f4
# 94153dec-c39b-40d0-ae0e-88dcdaf1fc72
# bbc3efec-9d9a-49dd-95f7-d68bc2edf924
# 3f85491f-98f0-4c54-aebf-978c8d05219f
# aa86b28a-0190-4660-8f18-4345aac53f5b
# dcd8f72f-863a-42dd-9514-c6ad22c172df
# e58ddd2a-2470-4388-b054-43609e3c192d
# 62f12705-0aa1-4333-9a06-d4f228c41316
# 92cd6a58-d22f-4af5-9bb7-8e3d8e92446b
# f741a68c-b8d8-4b55-bbd8-5a3db7b69c3b
# 822dd171-af63-467e-8e26-405d6e5ea839
# 31b57113-9f9b-4f08-9b46-a60a96191022
# c01d3de1-f915-4a22-96ae-30d2bd2c19ce
# 02c3e91b-1634-4c50-8bcd-272225c9b3b6
# ac51c80b-cfe0-4ab0-86d0-77b759a2ec3c
# b6e43d0c-d5df-48ce-a06a-5c42b7abe5bf
# 861cec4f-5cc6-4c98-b022-988c3f3f2560
# aa7985ea-d196-48d3-9a1f-014d8f53f0b7
# 0b02b99b-787d-4ff0-b80e-dc07bde2bf39
# 0c997266-3b60-4165-bbc6-d2f2504bf330
# 8501c349-a385-4bcf-9dae-68e6a2c57c30
# 80212f6c-6c4d-4774-a8ff-eb8aa7c817f4
# 5331b3c5-4014-43ac-bf7b-10eb51c85f2f
# 2886c541-8274-4867-9c62-0108d33d32c3
# 8b6f7286-a289-4a6e-9cbd-9d6dbea8e676
# f33413d2-bfe5-4106-b207-4564c8d5476c
# a418edac-bba8-461f-8d24-9f142c7d0e60
# 1f567640-a231-4daf-8efd-314aca109def
# 8047a5c0-5851-4ae7-8357-9cb202628ec3
# 40b092cf-3588-43c2-b054-27a663585935
# 335aa4b4-849b-4219-8971-f05d79ecd645
# e8de2158-88bd-406c-b15d-7e87db183d06
# 226b3e59-7183-407f-9beb-f11d623d3d59
# 4474f972-b96e-42ed-a37f-c07c75cddfb7
# d29c4fd3-45f8-4106-a1b6-a169058a74ef
# 109f1cb5-0299-48ad-8060-d071d0ea48e2
# 310a8735-bae9-4809-a7f3-17da55dd2189
# e9a948e8-abfa-4bb7-9ca1-27c52bfe9cbb
# 689f7ca3-54ca-4719-9511-18f5f7ac8cf6
# 766bc91c-1f31-4b5d-9346-b0f9b79d1967
# 6d4a379b-bce7-4632-928d-51566ddf494e
# 50ce6e1c-9d9d-427c-b7d0-4c92cb36a0cf


class DemoData:
  def __init__(self):
    self.users = []
    self.facilities = []
    self.medications = []
    self.activities = []
    self.contacts = []
    self.questions = []
    self.responses = []
    self.tasks = []
    self.surveys = []
    self.appointments = []
    self.schedules = []

  def create_task(self):

    tasks_data = [
      {
        "taskid": "3d6f9618-df4d-4a3f-b1a8-abc12918df13",
        "userid": "094f0422-bad1-4f36-8ae0-4286012d8109",
        "type": "taskType1",
        "extid": "ext123",
        "due_dt": "2023-04-25",
        "completed_dt": None,
        "status": "ongoing",
        "created_dt": "2023-03-31",
        "data": {"detail": "task detail 1"},
        "surveyid": None,
        "appointmentid": None,
        "medicationid": None,
        "scheduleid": None
      },
      {
        "taskid": "4c6e9618-df4d-4a3f-b785-abc12918df14",
        "userid": "2a10bfe7-ee4c-4760-8c70-cbd5bc80a47a",
        "type": "taskType2",
        "extid": "ext124",
        "due_dt": "2023-04-26",
        "completed_dt": "2023-04-01",
        "status": "completed",
        "created_dt": "2023-03-31",
        "data": {"detail": "task detail 2"},
        "surveyid": None,
        "appointmentid": None,
        "medicationid": None,
        "scheduleid": None
      },
      {
        "taskid": "5d6f9618-df4d-4a3f-b1a8-abc12918df15",
        "userid": "68df4738-4c0b-413d-b0d2-1d7f83df50fe",
        "type": "taskType3",
        "extid": "ext125",
        "due_dt": "2023-04-27",
        "completed_dt": None,
        "status": "ongoing",
        "created_dt": "2023-03-31",
        "data": {"detail": "task detail 3"},
        "surveyid": None,
        "appointmentid": None,
        "medicationid": None,
        "scheduleid": None
      },
      {
        "taskid": "6e6f9618-df4d-4a3f-b1a8-abc12918df16",
        "userid": "f41a60dc-2244-4875-838b-05167c9b5fb0",
        "type": "taskType4",
        "extid": "ext126",
        "due_dt": "2023-04-28",
        "completed_dt": "2023-04-01",
        "status": "completed",
        "created_dt": "2023-03-31",
        "data": {"detail": "task detail 4"},
        "surveyid": "45cd4b8b-8757-43f1-b5f8-76c9cbdbe8a1",
        "appointmentid": None,
        "medicationid": None,
        "scheduleid": None
      },
      {
        "taskid": "7f6f9618-df4d-4a3f-b1a8-abc12918df17",
        "userid": "eddca073-6d69-477e-97e3-71b18b926c50",
        "type": "taskType5",
        "extid": "ext127",
        "due_dt": "2023-04-29",
        "completed_dt": None,
        "status": "ongoing",
        "created_dt": "2023-03-31",
        "data": {"detail": "task detail 5"},
        "surveyid": None,
        "appointmentid": None,
        "medicationid": None,
        "scheduleid": None
      }
    ]

    for data in tasks_data:
      task = TaskBase(**data)
      self.tasks.append(task)
      try:
        existing_task = get_task(task.taskid)
        print("Found task, updating {}".format(task.taskid))
        update_task(task.taskid, task)
      except Exception as e:
        print("User not found, creating {}".format(task.taskid))
        create_task(task)

  def create_survey(self):
    #
    #
    #
    #
    #
    # dc53180d-6bf6-4d11-996e-50f505763936
    # 69eedc33-84ba-4ddf-91f7-fcb9fff549a8
    # b1960598-05c2-4a9c-a782-1993d13309ba
    surveys_data = [
      {
        "surveyid": "45cd4b8b-8757-43f1-b5f8-76c9cbdbe8a1",
        "title": "Survey 1",
        "description": "This is the first survey.",
        "created_dt": "2023-03-30",
        "data": {"question": "What is your favorite color?"},
        "final_msg": "Thank you for completing the survey!"
      },
      {
        "surveyid": "d04e2460-f89a-4488-af55-b8fcc13e3955",
        "title": "Survey 2",
        "description": "This is the second survey.",
        "created_dt": "2023-03-31",
        "data": {"question": "What is your favorite animal?"},
        "final_msg": "Your response has been recorded. Thank you!"
      },
      {
        "surveyid": "c93d2359-e999-4477-af54-a7ebc12f3844",
        "title": "Survey 3",
        "description": None,
        "created_dt": "2023-04-01",
        "data": {"question": "What is your favorite food?"},
        "final_msg": "We appreciate your time spent on this survey."
      },
      {
        "surveyid": "b82c2248-d898-4466-af53-a6dbf11e3733",
        "title": "Survey 4",
        "description": "This is the fourth survey.",
        "created_dt": "2023-04-02",
        "data": {"question": "What is your favorite place to visit?"},
        "final_msg": None
      },
      {
        "surveyid": "a81b2237-c897-4455-af52-a5dae10d3722",
        "title": "Survey 5",
        "description": None,
        "created_dt": "2023-04-03",
        "data": {"question": "What is your favorite hobby?"},
        "final_msg": "Your participation is greatly appreciated. Thank you!"
      }
    ]

    for data in surveys_data:
      survey = SurveyBase(**data)
      self.surveys.append(survey)
      try:
        existing_survey = get_survey(survey.surveyid)
        print("Found survey, updating {}".format(survey.surveyid))
        update_survey(survey.surveyid, survey)
      except Exception as e:
        print("User not found, creating {}".format(survey.surveyid))
        create_survey(survey)

  def create_session(self):

    sessions_data = [{}]

    for data in sessions_data:
      session = SessionBase(**data)
      self.sessions.append(session)
      try:
        existing_session = get_session(session.sessionid)
        print("Found session, updating {}".format(session.sessionid))
        update_session(session.sessionid, session)
      except Exception as e:
        print("User not found, creating {}".format(session.sessionid))
        create_session(session)

  def create_schedule(self):
    #
    #
    #
    #
    #
    # b5de52bb-1cca-4e3a-a15b-f46b2b50d5cb
    # 4481c2f0-f385-451a-88c8-e12fedbaead5
    # 5bda2fc8-75ab-4a77-9c66-30f170ba109e
    # 7d093e63-0c22-4685-bcae-4f732de7bded
    schedules_data = [
      {
        "scheduleid": "0f92d24b-d657-4570-a6ac-d680f119a722",
        "label": "Work Schedule",
        "type": "Work",
        "userid": "094f0422-bad1-4f36-8ae0-4286012d8109",
        "dow_mask": "MTWTF--",
        "start_dt": "2023-04-01",
        "end_dt": "2023-04-30",
        "repeats": True,
        "data": None
      },
      {
        "scheduleid": "a8ccd4c3-e887-4d81-aaea-9109580735d7",
        "label": "Gym Schedule",
        "type": "Exercise",
        "userid": "2a10bfe7-ee4c-4760-8c70-cbd5bc80a47a",
        "dow_mask": "M-W-F--",
        "start_dt": "2023-04-01",
        "end_dt": "2023-04-30",
        "repeats": True,
        "data": None
      },
      {
        "scheduleid": "db89123c-82a5-40be-8ea2-90f37035dc89",
        "label": "Study Schedule",
        "type": "Study",
        "userid": "68df4738-4c0b-413d-b0d2-1d7f83df50fe",
        "dow_mask": "-T-T---",
        "start_dt": "2023-04-01",
        "end_dt": "2023-04-30",
        "repeats": True,
        "data": None
      },
      {
        "scheduleid": "487c9037-8cc1-464b-a830-4eab9a624a73",
        "label": "Meditation Schedule",
        "type": "Meditation",
        "userid": "f41a60dc-2244-4875-838b-05167c9b5fb0",
        "dow_mask": "MTWTFSS",
        "start_dt": "2023-04-01",
        "end_dt": "2023-04-30",
        "repeats": True,
        "data": None
      },
      {
        "scheduleid": "67e1fd1c-0470-4b34-96cd-3197d40df29c",
        "label": "Reading Schedule",
        "type": "Reading",
        "userid": "eddca073-6d69-477e-97e3-71b18b926c50",
        "dow_mask": "---TFSS",
        "start_dt": "2023-04-01",
        "end_dt": "2023-04-30",
        "repeats": True,
        "data": None
      }
    ]

    for data in schedules_data:
      schedule = ScheduleBase(**data)
      self.schedules.append(schedule)
      try:
        existing_schedule = get_schedule(schedule.scheduleid)
        print("Found schedule, updating {}".format(schedule.scheduleid))
        update_schedule(schedule.scheduleid, schedule)
      except Exception as e:
        print("User not found, creating {}".format(schedule.scheduleid))
        create_schedule(schedule)

  def create_response(self):

    #
    #
    #
    #
    #
    #
    #
    #
    #
    #

    responses_data = [
      {
        "responseid": "a4a07a0e-7db6-487b-83dd-616d3d4382f2",
        "userid": "094f0422-bad1-4f36-8ae0-4286012d8109",
        "surveyid": "a81b2237-c897-4455-af52-a5dae10d3722",
        "questionid": "a91b3357-c998-4455-bf52-a5dae20c3732",
        "answers": "Red",
        "other": None,
        "skipped": False
      },
      {
        "responseid": "e0478a7b-6264-410c-abe8-599766aeb13b",
        "userid": "2a10bfe7-ee4c-4760-8c70-cbd5bc80a47a",
        "surveyid": "b82c2248-d898-4466-af53-a6dbf11e3733",
        "questionid": "b22c4478-d999-4466-af53-a6dbf21d3733",
        "answers": "Dog",
        "other": None,
        "skipped": False
      },
      {
        "responseid": "80f8b5e5-17da-420e-a89b-17ced0be5218",
        "userid": "68df4738-4c0b-413d-b0d2-1d7f83df50fe",
        "surveyid": "c93d2359-e999-4477-af54-a7ebc12f3844",
        "questionid": "c33d5599-e159-4477-af54-a7ebc22e3844",
        "answers": "Pizza",
        "other": None,
        "skipped": False
      },
      {
        "responseid": "850b0e9b-39d4-4716-8a05-523252ba8965",
        "userid": "f41a60dc-2244-4875-838b-05167c9b5fb0",
        "surveyid": "d04e2460-f89a-4488-af55-b8fcc13e3955",
        "questionid": "d44e6690-f2aa-4488-af55-b8fcc23f3955",
        "answers": "5",
        "other": None,
        "skipped": False
      },
      {
        "responseid": "84b37e75-98cd-4f58-822b-d1736b81521c",
        "userid": "eddca073-6d69-477e-97e3-71b18b926c50",
        "surveyid": "45cd4b8b-8757-43f1-b5f8-76c9cbdbe8a1",
        "questionid": "e024416c-3d3f-4eaf-bf99-b44894d238bd",
        "answers": "Through a friend",
        "other": None,
        "skipped": False
      }
    ]

    #
    # a35c4895-bf96-49f1-b1e5-e0c38f2509a1
    # 2e5950d9-ea8c-4e51-ad3d-c75dd13d4406
    # 0c455362-f1fe-47bf-b216-68a371e622dc

    for data in responses_data:
      response = ResponseBase(**data)
      self.responses.append(response)
      try:
        existing_response = get_response(response.responseid)
        print("Found response, updating {}".format(response.responseid))
        update_response(response.responseid, response)
      except Exception as e:
        print("User not found, creating {}".format(response.responseid))
        create_response(response)

  def create_question(self):

    questions_data = [
      {
        "questionid": "a91b3357-c998-4455-bf52-a5dae20c3732",
        "surveyid": "a81b2237-c897-4455-af52-a5dae10d3722",
        "type": "choice",
        "question": "What is your favorite color?",
        "possible_responses": "Red,Blue,Green,Yellow",
        "data": None,
        "multiple_choice": False,
        "has_other": True,
        "other_label": "Other, please specify:",
        "sequence": 1
      },
      {
        "questionid": "b22c4478-d999-4466-af53-a6dbf21d3733",
        "surveyid": "b82c2248-d898-4466-af53-a6dbf11e3733",
        "type": "choice",
        "question": "What is your favorite animal?",
        "possible_responses": "Dog,Cat,Bird,Fish",
        "data": None,
        "multiple_choice": False,
        "has_other": False,
        "other_label": None,
        "sequence": 1
      },
      {
        "questionid": "c33d5599-e159-4477-af54-a7ebc22e3844",
        "surveyid": "c93d2359-e999-4477-af54-a7ebc12f3844",
        "type": "open",
        "question": "What is your favorite food?",
        "possible_responses": None,
        "data": None,
        "multiple_choice": False,
        "has_other": False,
        "other_label": None,
        "sequence": 1
      },
      {
        "questionid": "d44e6690-f2aa-4488-af55-b8fcc23f3955",
        "surveyid": "d04e2460-f89a-4488-af55-b8fcc13e3955",
        "type": "rating",
        "question": "How much do you like our service?",
        "possible_responses": "1,2,3,4,5",
        "data": None,
        "multiple_choice": False,
        "has_other": False,
        "other_label": None,
        "sequence": 1
      },
      {
        "questionid": "e024416c-3d3f-4eaf-bf99-b44894d238bd",
        "surveyid": "45cd4b8b-8757-43f1-b5f8-76c9cbdbe8a1",
        "type": "open",
        "question": "How did you hear about us?",
        "possible_responses": None,
        "data": None,
        "multiple_choice": False,
        "has_other": False,
        "other_label": None,
        "sequence": 1
      }
    ]

    for data in questions_data:
      question = QuestionBase(**data)
      self.questions.append(question)
      try:
        existing_question = get_question(question.questionid)
        print("Found question, updating {}".format(question.questionid))
        update_question(question.questionid, question)
      except Exception as e:
        print("User not found, creating {}".format(question.questionid))
        create_question(question)

  def create_contact(self):
    #
    #
    #
    #
    #
    contacts_data = [
      {
        "contactid": "094f0422-bad1-4f36-8ae0-4286012d8109",
        "userid": "094f0422-bad1-4f36-8ae0-4286012d8109",
        "contact_extid": "2a10bfe7-ee4c-4760-8c70-cbd5bc80a47a",
        "contact_label": "Friend"
      },
      {
        "contactid": "72de3b47-3911-4397-81df-36444bdd6e63",
        "userid": "2a10bfe7-ee4c-4760-8c70-cbd5bc80a47a",
        "contact_extid": "68df4738-4c0b-413d-b0d2-1d7f83df50fe",
        "contact_label": "Coworker"
      },
      {
        "contactid": "3c999b6a-2648-4545-93e7-aeb62d4abf60",
        "userid": "68df4738-4c0b-413d-b0d2-1d7f83df50fe",
        "contact_extid": "f41a60dc-2244-4875-838b-05167c9b5fb0",
        "contact_label": "Family"
      },
      {
        "contactid": "995d6c04-fa2b-4ad5-8a2f-9b72cda2a015",
        "userid": "f41a60dc-2244-4875-838b-05167c9b5fb0",
        "contact_extid": "eddca073-6d69-477e-97e3-71b18b926c50",
        "contact_label": "Friend"
      },
      {
        "contactid": "76d679e2-3b10-4965-9706-b41b33011b82",
        "userid": "eddca073-6d69-477e-97e3-71b18b926c50",
        "contact_extid": "094f0422-bad1-4f36-8ae0-4286012d8109",
        "contact_label": "Coworker"
      }
    ]

    for data in contacts_data:
      contact = ContactBase(**data)
      self.contacts.append(contact)
      try:
        existing_contact = get_contact(contact.contactid)
        print("Found contact, updating {}".format(contact.contactid))
        update_contact(contact.contactid, contact)
      except Exception as e:
        print("User not found, creating {}".format(contact.contactid))
        create_contact(contact)

  def create_appointments(self):

    #
    #
    #
    #
    #
    #
    # 9c07fbf9-e275-476a-be40-3cb0d6fbda5a
    # fa0cba75-2669-4d2b-9868-8eddf45b7311
    # 2694b72c-28d2-4d5b-9244-c2de523b746f
    # c40916f3-eca5-4632-832a-31533f41e4e8
    # 863b47d0-7c77-4d6e-bb90-5fc760b25d03
    # ce0a4909-1124-480a-93ed-d0a312e16839
    # df0fe121-2de6-4fdd-8678-53168acb3b8e

    appointments_data = [
      {
        "appointmentid": "211343cd-e489-4ca1-8ec4-7838c427715e",
        "userid": "094f0422-bad1-4f36-8ae0-4286012d8109",
        "start_date": "2023-05-01",
        "end_date": "2023-05-01",
        "location": "Hospital A",
        "physician": "Dr. John Smith",
        "reason": "Routine Checkup",
        "reason_es": "Revisión de rutina",
        "confirmed": True,
        "confirmed_dt": "2023-04-20",
        "reschedule_phone": "123-456-7890",
        "cancelled": False,
        "cancelled_dt": None,
        "days_reminder": 7
      },
      {
        "appointmentid": "043f0232-612d-40e2-8f79-eed547452e10",
        "userid": "094f0422-bad1-4f36-8ae0-4286012d8109",
        "start_date": "2023-06-01",
        "end_date": "2023-06-01",
        "location": "Hospital A",
        "physician": "Dr. John Smith",
        "reason": "Follow-Up",
        "reason_es": "Seguimiento",
        "confirmed": False,
        "confirmed_dt": None,
        "reschedule_phone": "123-456-7890",
        "cancelled": False,
        "cancelled_dt": None,
        "days_reminder": 7
      },
      {
        "appointmentid": "820569ea-18ea-4eaf-a2ed-ae3ed68e17e4",
        "userid": "094f0422-bad1-4f36-8ae0-4286012d8109",
        "start_date": "2023-07-01",
        "end_date": "2023-07-01",
        "location": "Hospital A",
        "physician": "Dr. John Smith",
        "reason": "Follow-Up",
        "reason_es": "Seguimiento",
        "confirmed": False,
        "confirmed_dt": None,
        "reschedule_phone": "123-456-7890",
        "cancelled": False,
        "cancelled_dt": None,
        "days_reminder": 7
      },
      {
        "appointmentid": "cf83e400-9960-4794-9d20-188f8fd71aee",
        "userid": "2a10bfe7-ee4c-4760-8c70-cbd5bc80a47a",
        "start_date": "2023-05-02",
        "end_date": "2023-05-02",
        "location": "Hospital B",
        "physician": "Dr. Jane Doe",
        "reason": "Blood Test",
        "reason_es": "Análisis de sangre",
        "confirmed": True,
        "confirmed_dt": "2023-04-22",
        "reschedule_phone": "234-567-8901",
        "cancelled": False,
        "cancelled_dt": None,
        "days_reminder": 5
      },
      {
        "appointmentid": "9e2e9546-6f8e-4f0c-b20f-2ae4434281b9",
        "userid": "2a10bfe7-ee4c-4760-8c70-cbd5bc80a47a",
        "start_date": "2023-06-02",
        "end_date": "2023-06-02",
        "location": "Hospital B",
        "physician": "Dr. Jane Doe",
        "reason": "Heart Checkup",
        "reason_es": "Chequeo de corazón",
        "confirmed": False,
        "confirmed_dt": None,
        "reschedule_phone": "234-567-8901",
        "cancelled": False,
        "cancelled_dt": None,
        "days_reminder": 5
      },
      {
        "appointmentid": "d5348515-ddaf-44a4-902a-ed90f87e58e5",
        "userid": "68df4738-4c0b-413d-b0d2-1d7f83df50fe",
        "start_date": "2023-05-03",
        "end_date": "2023-05-03",
        "location": "Hospital C",
        "physician": "Dr. Robert Taylor",
        "reason": "Vaccination",
        "reason_es": "Vacunación",
        "confirmed": True,
        "confirmed_dt": "2023-04-25",
        "reschedule_phone": "456-789-0123",
        "cancelled": False,
        "cancelled_dt": None,
        "days_reminder": 10
      }
    ]

    for data in appointments_data:
      appointment = AppointmentBase(**data)
      self.appointments.append(appointment)
      try:
        existing_appointment = get_appointment(appointment.appointmentid)
        print("Found appointment, updating {}".format(appointment.appointmentid))
        update_appointment(appointment.appointmentid, appointment)
      except Exception as e:
        print("User not found, creating {}".format(appointment.appointmentid))
        create_appointment(appointment)

  def create_medications(self):

    medications_data = [
      {
        "medicationid": "3c5ae13e-758b-4a92-ae25-65bc9301f450",
        "userid": "094f0422-bad1-4f36-8ae0-4286012d8109",
        "from_dt": "2024-01-01",
        "until_dt": "2024-01-31",
        "label": "Aspirin",
        "prescription": "Take one tablet daily with food.",
        "take_dow_mask": None,
        "dosage_info": "325 mg",
        "usage_info": "For pain relief and reducing fever.",
        "warnings_info": "Do not take if allergic to aspirin."
      },
      {
        "medicationid": "4f996543-892d-40a2-bb7e-5db402ff828c",
        "userid": "2a10bfe7-ee4c-4760-8c70-cbd5bc80a47a",
        "from_dt": "2024-02-01",
        "until_dt": "2024-02-28",
        "label": "Lisinopril",
        "prescription": "Take one tablet daily in the morning.",
        "take_dow_mask": None,
        "dosage_info": "10 mg",
        "usage_info": "For controlling blood pressure.",
        "warnings_info": "May cause dizziness. Avoid alcohol."
      },
      {
        "medicationid": "fc28cb05-36d5-4b16-a127-86b3d94c79b1",
        "userid": "68df4738-4c0b-413d-b0d2-1d7f83df50fe",
        "from_dt": "2024-01-15",
        "until_dt": "2024-03-15",
        "label": "Omeprazole",
        "prescription": "Take one capsule daily before breakfast.",
        "take_dow_mask": None,
        "dosage_info": "20 mg",
        "usage_info": "For treating acid reflux and heartburn.",
        "warnings_info": "Do not crush or chew capsules."
      },
      {
        "medicationid": "824f02a1-9c5c-4746-a7f3-ef3398239ef7",
        "userid": "f41a60dc-2244-4875-838b-05167c9b5fb0",
        "from_dt": "2024-02-01",
        "until_dt": "2024-02-28",
        "label": "Simvastatin",
        "prescription": "Take one tablet daily at bedtime.",
        "take_dow_mask": None,
        "dosage_info": "20 mg",
        "usage_info": "For lowering cholesterol levels.",
        "warnings_info": "Avoid grapefruit juice while taking this medication."
      },
      {
        "medicationid": "cd29bb35-f27e-46f7-9d61-90e0e11b06b3",
        "userid": "eddca073-6d69-477e-97e3-71b18b926c50",
        "from_dt": "2024-01-01",
        "until_dt": "2024-01-31",
        "label": "Ibuprofen",
        "prescription": "Take one tablet every 4-6 hours as needed for pain.",
        "take_dow_mask": None,
        "dosage_info": "200 mg",
        "usage_info": "For relief of minor aches and pains.",
        "warnings_info": "Do not exceed recommended dosage."
      }
    ]

    for data in medications_data:
      medication = MedicationBase(**data)
      self.medications.append(medication)
      try:
        existing_medication = get_medication(medication.medicationid)
        print("Found medication, updating {}".format(medication.medicationid))
        update_medication(medication.medicationid, medication)
      except Exception as e:
        print("User not found, creating {}".format(medication.medicationid))
        create_medication(medication)

  def create_facilities(self):
    facilities_data = [
      {
        "facilityid": "eac2bc3f-0ae5-45a4-bdcd-829a69dc9e68",
        "facility": "City General Hospital",
        "address": "123 Main Street, Cityville, USA",
        "type": "Hospital",
        "logo_url": "https://example.com/logo1.png",
        "photo_url": "https://example.com/photo1.png"
      },
      {
        "facilityid": "2b4c659d-78d6-4389-9b53-4d446b932f18",
        "facility": "Suburban Medical Center",
        "address": "456 Oak Avenue, Suburbia, USA",
        "type": "Medical Center",
        "logo_url": "https://example.com/logo2.png",
        "photo_url": "https://example.com/photo2.png"
      },
      {
        "facilityid": "a1fdce5a-8997-4ff0-ae7a-1875fd2c3614",
        "facility": "Rural Clinic",
        "address": "789 Elm Street, Countryside, USA",
        "type": "Clinic",
        "logo_url": "https://example.com/logo3.png",
        "photo_url": "https://example.com/photo3.png"
      }
    ]

    for data in facilities_data:
      facility = FacilityBase(**data)
      self.facilities.append(facility)
      try:
        existing_facility = get_facility(facility.facilityid)
        print("Found facility, updating {}".format(facility.facilityid))
        update_facility(facility.facilityid, facility)
      except Exception as e:
        print("Facility not found, creating {}".format(facility.facilityid))
        create_facility(facility)

  def create_users(self):
    user_data = [
      {
        "userid": "094f0422-bad1-4f36-8ae0-4286012d8109",
        "type": "patient",
        "is_patient": True,
        "first_name": "John",
        "last_name": "Doe",
        "username": "johndoe",
        "last_login_dt": "2023-01-01",
        "contact_information": "john@example.com",
        "patientid": "",
        "pass_hash": hashlib.md5("password1".encode()).hexdigest(),
        "other_information": "",
        "extid": "",
        "department": "",
        "location": "",
        "suffix": "",
        "prefix": "",
        "affiliated_facilityid": None,
        "photo_url": ""
      },
      {
        "userid": "2a10bfe7-ee4c-4760-8c70-cbd5bc80a47a",
        "type": "patient",
        "is_patient": True,
        "first_name": "Alice",
        "last_name": "Smith",
        "username": "alicesmith",
        "last_login_dt": "2023-01-01",
        "contact_information": "alice@example.com",
        "patientid": "",
        "pass_hash": hashlib.md5("password2".encode()).hexdigest(),
        "other_information": "",
        "extid": "",
        "department": "",
        "location": "",
        "suffix": "",
        "prefix": "",
        "affiliated_facilityid": None,
        "photo_url": ""
      },
      {
        "userid": "68df4738-4c0b-413d-b0d2-1d7f83df50fe",
        "type": "patient",
        "is_patient": True,
        "first_name": "Emily",
        "last_name": "Johnson",
        "username": "emilyjohnson",
        "last_login_dt": "2023-01-01",
        "contact_information": "emily@example.com",
        "patientid": "",
        "pass_hash": hashlib.md5("password3".encode()).hexdigest(),
        "other_information": "",
        "extid": "",
        "department": "",
        "location": "",
        "suffix": "",
        "prefix": "",
        "affiliated_facilityid": None,
        "photo_url": ""
      },
      {
        "userid": "f41a60dc-2244-4875-838b-05167c9b5fb0",
        "type": "physician",
        "is_patient": True,
        "first_name": "Michael",
        "last_name": "Brown",
        "username": "michaelbrown",
        "last_login_dt": "2023-01-01",
        "contact_information": "michael@example.com",
        "patientid": "",
        "pass_hash": hashlib.md5("password4".encode()).hexdigest(),
        "other_information": "",
        "extid": "",
        "department": "",
        "location": "",
        "suffix": "",
        "prefix": "",
        "affiliated_facilityid": None,
        "photo_url": ""
      },
      {
        "userid": "eddca073-6d69-477e-97e3-71b18b926c50",
        "type": "admin",
        "is_patient": False,
        "first_name": "Sophia",
        "last_name": "Williams",
        "username": "sophiawilliams",
        "last_login_dt": "2023-01-01",
        "contact_information": "sophia@example.com",
        "patientid": "",
        "pass_hash": hashlib.md5("password5".encode()).hexdigest(),
        "other_information": "",
        "extid": "",
        "department": "",
        "location": "",
        "suffix": "",
        "prefix": "",
        "affiliated_facilityid": None,
        "photo_url": ""
      }
    ]

    for data in user_data:
      user = UserBase(**data)
      self.users.append(user)
      try:
        existing_user = get_user(user.userid)
        print("Found user, updating {}".format(user.userid))
        update_user(user.userid, user)
      except Exception as e:
        print("User not found, creating {}".format(user.userid))
        create_user(user)

  def print_users(self):
    for user in self.users:
      print(user.dict())

  def print_medications(self):
    for medication in self.medications:
      print(medication.dict())

  def print_facilities(self):
    for facility in self.facilities:
      print(facility.dict())
