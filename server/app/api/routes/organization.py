from fastapi import APIRouter, Depends, status, Body, HTTPException
from fastapi.exceptions import HTTPException
from typing import List
from sqlalchemy.orm import Session

from ...db.db import get_session
from ..repositories.organization import OrganizationRepository
from ..dependencies.database import get_repository
from ...models.organization import *
from ...models.user import *


router = APIRouter()

@router.post('/', response_model=Organization, status_code=status.HTTP_201_CREATED)
def create_organization(
    new_organization: OrganizationCreate,
    session: Session = Depends(get_session)
    ):

    organization = Organization(**new_organization.dict())

    print('organization', organization)
    user = session.get(User, new_organization.created_by)
    print('user', user)

    organization.created_by = user
    # organization.users.append(user)

    print('organization after', organization)

    session.add(organization)

    session.commit()
    session.refresh(organization)

    return organization


# @router.post('/', response_model=Organization, status_code=status.HTTP_201_CREATED)
# def create_organization(
#     organization: OrganizationCreate,
#     organization_repository: OrganizationRepository = Depends(
#         get_repository(OrganizationRepository))
#     ):
#     return organization_repository.create_organization(new_organization=organization)

# @router.get('/get_organization_by_id', response_model=OrganizationRead)
# def get_organization(
#     organization_id: int,
#     organization_repository: OrganizationRepository = Depends(
#         get_repository(OrganizationRepository))
#     ):

#     return organization_repository.get_organization(organization_id=organization_id)


# @router.get('/get_organization_by_user/{user_id}', response_model=List[OrganizationRead])
# def get_organization_of_user(
#     user_id: int,
#     organization_repository: OrganizationRepository = Depends(
#         get_repository(OrganizationRepository))
#     ):
#     res = organization_repository.get_organizations_for_user(user_id=user_id)
#     return res

# @router.post('/add_user', response_model=OrganizationRead)
# def add_user_to_organization(
#     organization_id: int,
#     user_id: int,
#     permissions: str = None,
#     organization_repository: OrganizationRepository = Depends(
#         get_repository(OrganizationRepository))
#     ):

#     return organization_repository.add_user(organization_id=organization_id, user_id=user_id, permissions=permissions)
