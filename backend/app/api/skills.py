from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..dependencies import get_current_active_user

router = APIRouter(prefix="/skills", tags=["skills"])

@router.post("/", response_model=schemas.SkillResponse)
def create_skill(
    skill: schemas.SkillCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user)
):
    """Create a new skill."""
    db_skill = crud.create_skill(db=db, skill=skill, owner_id=current_user.id)
    return crud.skill_to_response(db_skill)

@router.get("/", response_model=List[schemas.SkillResponse])
def get_skills(
    skip: int = 0,
    limit: int = 100,
    owner_id: int = None,
    db: Session = Depends(get_db)
):
    """Get all skills with optional filtering by owner."""
    skills = crud.get_skills(db, skip=skip, limit=limit, owner_id=owner_id)
    return [crud.skill_to_response(skill) for skill in skills]

@router.get("/{skill_id}", response_model=schemas.SkillResponse)
def get_skill(skill_id: int, db: Session = Depends(get_db)):
    """Get a specific skill by ID."""
    skill = crud.get_skill(db, skill_id=skill_id)
    if skill is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found"
        )
    return crud.skill_to_response(skill)

@router.put("/{skill_id}", response_model=schemas.SkillResponse)
def update_skill(
    skill_id: int,
    skill_update: schemas.SkillUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user)
):
    """Update a skill (only by owner)."""
    skill = crud.update_skill(db, skill_id, skill_update, current_user.id)
    if skill is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found or you don't have permission to update it"
        )
    return crud.skill_to_response(skill)

@router.delete("/{skill_id}")
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user)
):
    """Delete a skill (only by owner)."""
    success = crud.delete_skill(db, skill_id, current_user.id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found or you don't have permission to delete it"
        )
    return {"message": "Skill deleted successfully"}

@router.get("/my-skills/", response_model=List[schemas.SkillResponse])
def get_my_skills(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user)
):
    """Get current user's skills."""
    skills = crud.get_skills(db, skip=skip, limit=limit, owner_id=current_user.id)
    return [crud.skill_to_response(skill) for skill in skills]

