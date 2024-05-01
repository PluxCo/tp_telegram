from sqlalchemy.orm import Mapped, mapped_column

from core.message import Message, MessageState as EntityMessageState
from domain.model.message_model import MotivationMessageModel, MessageState
from domain.model.user_model import UserModel


class MotivationMessageEntity(Message):
    __mapper_args__ = {'polymorphic_identity': 'motivation'}

    mood: Mapped[str] = mapped_column(nullable=True)

    def to_model(self, assigned_user: UserModel) -> MotivationMessageModel:
        return MotivationMessageModel(id=self.id, user=assigned_user, service_id=self.service_id,
                                      date=self.date,
                                      state=MessageState.SENT if self.state == EntityMessageState.TRANSFERRED else MessageState.PENDING,
                                      mood=self.mood)
