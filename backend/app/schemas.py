from pydantic import BaseModel, computed_field
from typing import List, Optional
from datetime import datetime

# Try to import EmailStr, fallback to str if not available
try:
    from pydantic import EmailStr
    EmailType = EmailStr
except ImportError:
    EmailType = str

# User schemas
class UserBase(BaseModel):
    username: str
    email: EmailType

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Tag schemas
class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int
    
    class Config:
        from_attributes = True

# Skill schemas
class SkillBase(BaseModel):
    title: str
    description: str
    difficulty: str = "beginner"

class SkillCreate(SkillBase):
    tags: Optional[List[str]] = []

class SkillUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    difficulty: Optional[str] = None
    tags: Optional[List[str]] = None

class Skill(SkillBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    tags: List[Tag] = []
    
    class Config:
        from_attributes = True

class SkillResponse(BaseModel):
    id: int
    title: str
    description: str
    difficulty: str
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    tags: List[str] = []
    
    @computed_field
    @property
    def tag_names(self) -> List[str]:
        """Convert Tag objects to tag names for response."""
        return [tag.name if hasattr(tag, 'name') else str(tag) for tag in self.tags]
    
    class Config:
        from_attributes = True

# Message schemas
class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    receiver_id: int

class Message(MessageBase):
    id: int
    sender_id: int
    receiver_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
