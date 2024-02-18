from sqlalchemy import Column, String, Date, Boolean, JSON, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


# Activity log
class Activity(Base):
  __tablename__ = 'activity'
  activityid = Column(UUID(as_uuid=True), primary_key=True)
  type = Column(String(50), nullable=False)
  occurence_dt = Column(Date, nullable=False)
  extid = Column(String(200))
  label = Column(String(100), nullable=False)
  description = Column(String(500))
  icon = Column(String(50))


class Users(Base):
  __tablename__ = 'users'
  userid = Column(UUID(as_uuid=True), primary_key=True)
  type = Column(String(20), nullable=False)
  is_patient = Column(Boolean, default=True, nullable=False)
  first_name = Column(String(50), nullable=False)
  last_name = Column(String(50), nullable=False)
  patientid = Column(String(50))
  pass_hash = Column(String(50))
  last_login_dt = Column(Date)
  contact_information = Column(String(500))
  other_information = Column(String(500))
  extid = Column(String(100))
  department = Column(String(50))
  location = Column(String(100))
  suffix = Column(String(10))
  prefix = Column(String(10))
  affiliated_facilityid = Column(UUID(as_uuid=True))
  photo_url = Column(String(200))
  username = Column(String(30), nullable=False)
  # Relationships
  tasks = relationship('Task', backref='users')
  responses = relationship('Response', backref='users')
  appointments = relationship('Appointment', backref='users')
  contacts = relationship('Contact', backref='users')
  medications = relationship('Medication', backref='users')
  schedules = relationship('Schedule', backref='users')
  sessions = relationship('Session', backref='users')


class Appointment(Base):
  __tablename__ = 'appointment'
  appointmentid = Column(UUID(as_uuid=True), primary_key=True)
  userid = Column(UUID(as_uuid=True), ForeignKey('users.userid'), nullable=False)
  start_date = Column(Date, nullable=False)
  end_date = Column(Date)
  location = Column(String(200))
  physician = Column(String(100))
  reason = Column(String(500))
  reason_es = Column(String(500))
  confirmed = Column(Boolean, default=False, nullable=False)
  confirmed_dt = Column(Date)
  reschedule_phone = Column(String(200))
  cancelled = Column(Boolean, default=False, nullable=False)
  cancelled_dt = Column(Date)
  days_reminder = Column(Integer, default=1, nullable=False)
  # Relationships
  #add this back later
  #tasks = relationship('Task', backref='appointment')


class Contact(Base):
  __tablename__ = 'contact'
  contactid = Column(UUID(as_uuid=True), primary_key=True)
  userid = Column(UUID(as_uuid=True), ForeignKey('users.userid'))
  contact_extid = Column(String(200))
  contact_label = Column(String(200))


class Facility(Base):
  __tablename__ = 'facility'
  facilityid = Column(UUID(as_uuid=True), primary_key=True)
  facility = Column(String(50))
  address = Column(String(100))
  type = Column(String(50))
  logo_url = Column(String(100))
  photo_url = Column(String(100))


class Medication(Base):
  __tablename__ = 'medication'
  medicationid = Column(UUID(as_uuid=True), primary_key=True)
  userid = Column(UUID(as_uuid=True), nullable=False)
  from_dt = Column(Date)
  until_dt = Column(Date)
  label = Column(String(100))
  prescription = Column(String, nullable=False)
  take_dow_mask = Column(String(7))
  dosage_info = Column(String(50))
  usage_info = Column(String(500))
  warnings_info = Column(String(500))
  # Foreign keys
  userid = Column(UUID(as_uuid=True), ForeignKey('users.userid'))
  # Relationships
  tasks = relationship('Task', backref='medication')


class Question(Base):
  __tablename__ = 'question'
  questionid = Column(UUID(as_uuid=True), primary_key=True)
  surveyid = Column(UUID(as_uuid=True), ForeignKey('survey.surveyid'),nullable=False)
  type = Column(String(50), nullable=False)
  question = Column(String(100), nullable=False)
  possible_responses = Column(String(500))
  data = Column(JSON)
  multiple_choice = Column(Boolean)
  has_other = Column(Boolean)
  other_label = Column(String)
  sequence = Column(Integer, default=1, nullable=False)
  # Foreign keys
  # Relationships
  responses = relationship('Response', backref='question')


class Schedule(Base):
  __tablename__ = 'schedule'
  scheduleid = Column(UUID(as_uuid=True), primary_key=True)
  label = Column(String)
  userid = Column(UUID(as_uuid=True), nullable=False)
  dow_mask = Column(String(7))
  start_dt = Column(Date)
  end_dt = Column(Date)
  repeats = Column(Boolean)
  type = Column(String)
  data = Column(JSON)
  # Foreign keys
  userid = Column(UUID(as_uuid=True), ForeignKey('users.userid'))
  # Relationships
  tasks = relationship('Task', backref='schedule')


class Session(Base):
  __tablename__ = 'session'
  sessionid = Column(UUID(as_uuid=True), primary_key=True)
  userid = Column(UUID(as_uuid=True), nullable=False)
  login_dt = Column(Date)
  exp_dt = Column(Date)
  # Foreign keys
  userid = Column(UUID(as_uuid=True), ForeignKey('users.userid'))


class Survey(Base):
  __tablename__ = 'survey'
  surveyid = Column(UUID(as_uuid=True), primary_key=True)
  title = Column(String(50), nullable=False)
  description = Column(String(200))
  created_dt = Column(Date)
  data = Column(JSON)
  final_msg = Column(String(200))


class Response(Base):
  __tablename__ = 'response'
  responseid = Column(UUID(as_uuid=True), primary_key=True)
  userid = Column(UUID(as_uuid=True), ForeignKey('users.userid'))
  surveyid = Column(UUID(as_uuid=True), ForeignKey('survey.surveyid'))
  questionid = Column(UUID(as_uuid=True), ForeignKey('question.questionid'))
  answers = Column(String(500))
  other = Column(String(500))
  skipped = Column(Boolean, default=False)


class Task(Base):
  __tablename__ = 'task'
  taskid = Column(UUID(as_uuid=True), primary_key=True)
  userid = Column(UUID(as_uuid=True), ForeignKey('users.userid'))
  type = Column(String(50))
  extid = Column(String(200))
  due_dt = Column(Date)
  completed_dt = Column(Date)
  status = Column(String(50))
  created_dt = Column(Date)
  data = Column(JSON)
  surveyid = Column(UUID(as_uuid=True), ForeignKey('survey.surveyid'))
  appointmentid = Column(UUID(as_uuid=True), ForeignKey('appointment.appointmentid'))
  medicationid = Column(UUID(as_uuid=True), ForeignKey('medication.medicationid'))
  scheduleid = Column(UUID(as_uuid=True), ForeignKey('schedule.scheduleid'))
  # Foreign keys
