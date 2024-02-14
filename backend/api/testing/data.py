import hashlib

from api.admin.users import UserBase
from api.admin.users import create_user, update_user, get_user


# Some UUIDs
# 094f0422-bad1-4f36-8ae0-4286012d8109
# 72de3b47-3911-4397-81df-36444bdd6e63
# 3c999b6a-2648-4545-93e7-aeb62d4abf60
# 995d6c04-fa2b-4ad5-8a2f-9b72cda2a015
# 76d679e2-3b10-4965-9706-b41b33011b82
# bd9d3015-1a6b-4ccd-8720-24c22406c6a1
# c310ffd4-d1cf-47a9-b497-4eeb4c0fd4d1
# a9d7c76f-40dd-454e-a263-d598c5d7f061
# ce814d52-a300-4304-b629-8d574b642de1
# 45cd4b8b-8757-43f1-b5f8-76c9cbdbe8a1
# dc53180d-6bf6-4d11-996e-50f505763936
# 69eedc33-84ba-4ddf-91f7-fcb9fff549a8
# b1960598-05c2-4a9c-a782-1993d13309ba
# e56e0fc1-c4dc-448f-82e3-826de8017e57
# acbb81bc-a0ef-4da2-85c9-1f6fb43c8e3c
# 28ea74c8-9235-43f5-af2e-9d28c9dc0aac
# bcabbc92-c582-4996-b83c-561dfd896a65
# d3e653a9-9bb3-410e-92a1-f7c85a82b16b
# e024416c-3d3f-4eaf-bf99-b44894d238bd
# a4a07a0e-7db6-487b-83dd-616d3d4382f2
# e0478a7b-6264-410c-abe8-599766aeb13b
# 80f8b5e5-17da-420e-a89b-17ced0be5218
# 850b0e9b-39d4-4716-8a05-523252ba8965
# 84b37e75-98cd-4f58-822b-d1736b81521c
# a35c4895-bf96-49f1-b1e5-e0c38f2509a1
# 2e5950d9-ea8c-4e51-ad3d-c75dd13d4406
# 0c455362-f1fe-47bf-b216-68a371e622dc
# 0f92d24b-d657-4570-a6ac-d680f119a722
# a8ccd4c3-e887-4d81-aaea-9109580735d7
# db89123c-82a5-40be-8ea2-90f37035dc89
# 67e1fd1c-0470-4b34-96cd-3197d40df29c
# 487c9037-8cc1-464b-a830-4eab9a624a73
# b5de52bb-1cca-4e3a-a15b-f46b2b50d5cb
# 4481c2f0-f385-451a-88c8-e12fedbaead5
# 5bda2fc8-75ab-4a77-9c66-30f170ba109e
# 7d093e63-0c22-4685-bcae-4f732de7bded
# 211343cd-e489-4ca1-8ec4-7838c427715e
# 043f0232-612d-40e2-8f79-eed547452e10
# 820569ea-18ea-4eaf-a2ed-ae3ed68e17e4
# cf83e400-9960-4794-9d20-188f8fd71aee
# 9e2e9546-6f8e-4f0c-b20f-2ae4434281b9
# d5348515-ddaf-44a4-902a-ed90f87e58e5
# 9c07fbf9-e275-476a-be40-3cb0d6fbda5a
# fa0cba75-2669-4d2b-9868-8eddf45b7311
# 2694b72c-28d2-4d5b-9244-c2de523b746f
# c40916f3-eca5-4632-832a-31533f41e4e8
# 863b47d0-7c77-4d6e-bb90-5fc760b25d03
# ce0a4909-1124-480a-93ed-d0a312e16839
# df0fe121-2de6-4fdd-8678-53168acb3b8e
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
        "type": "patient",
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
