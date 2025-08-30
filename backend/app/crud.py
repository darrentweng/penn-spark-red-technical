from sqlalchemy.orm import Session
from sqlalchemy import and_
from . import models, schemas
from .auth import get_password_hash, verify_password
from sqlalchemy import or_

# User CRUD operations
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user

# Tag CRUD operations
def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()

def get_tag_by_name(db: Session, name: str):
    return db.query(models.Tag).filter(models.Tag.name == name).first()

def get_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tag).offset(skip).limit(limit).all()

def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_or_create_tag(db: Session, tag_name: str):
    """Get existing tag or create new one."""
    tag = get_tag_by_name(db, tag_name)
    if tag:
        return tag
    return create_tag(db, schemas.TagCreate(name=tag_name))

# Skill CRUD operations
def get_skill(db: Session, skill_id: int):
    return db.query(models.Skill).filter(models.Skill.id == skill_id).first()

def get_skills(db: Session, skip: int = 0, limit: int = 100, owner_id: int = None):
    query = db.query(models.Skill)
    if owner_id:
        query = query.filter(models.Skill.owner_id == owner_id)
    return query.offset(skip).limit(limit).all()

def create_skill(db: Session, skill: schemas.SkillCreate, owner_id: int):
    # Create skill
    db_skill = models.Skill(
        title=skill.title,
        description=skill.description,
        difficulty=skill.difficulty,
        owner_id=owner_id
    )
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    
    # Add tags if provided
    if skill.tags:
        for tag_name in skill.tags:
            tag = get_or_create_tag(db, tag_name)
            db_skill.tags.append(tag)
        db.commit()
        db.refresh(db_skill)
    
    return db_skill

def update_skill(db: Session, skill_id: int, skill_update: schemas.SkillUpdate, owner_id: int):
    db_skill = get_skill(db, skill_id)
    if not db_skill:
        return None
    if db_skill.owner_id != owner_id:
        return None
    
    # Update basic fields
    update_data = skill_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        if field != "tags":
            setattr(db_skill, field, value)
    
    # Update tags if provided
    if skill_update.tags is not None:
        db_skill.tags.clear()
        for tag_name in skill_update.tags:
            tag = get_or_create_tag(db, tag_name)
            db_skill.tags.append(tag)
    
    db.commit()
    db.refresh(db_skill)
    return db_skill

def delete_skill(db: Session, skill_id: int, owner_id: int):
    db_skill = get_skill(db, skill_id)
    if not db_skill:
        return False
    if db_skill.owner_id != owner_id:
        return False
    
    db.delete(db_skill)
    db.commit()
    return True

# Message CRUD operations
def get_messages(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Message).filter(
        or_(models.Message.sender_id == user_id, models.Message.receiver_id == user_id)
    ).offset(skip).limit(limit).all()

def create_message(db: Session, message: schemas.MessageCreate, sender_id: int):
    db_message = models.Message(
        content=message.content,
        sender_id=sender_id,
        receiver_id=message.receiver_id
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

# Helper function to convert skill model to response format
def skill_to_response(skill: models.Skill) -> dict:
    """Convert skill model to response format with tag names."""
    return {
        "id": skill.id,
        "title": skill.title,
        "description": skill.description,
        "difficulty": skill.difficulty,
        "owner_id": skill.owner_id,
        "created_at": skill.created_at,
        "updated_at": skill.updated_at,
        "tags": [tag.name for tag in skill.tags]
    }

