from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,LargeBinary
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class USERS(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    username=Column(String(100),nullable=False)
    email=Column(String(100),nullable=False,unique=True)
    role=Column(String(50),nullable=False)
    password=Column(String(100),nullable=False)
    profile_photo=Column(LargeBinary,nullable=True)
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'profile_photo': self.profile_photo  # This can be handled separately if needed
        }
