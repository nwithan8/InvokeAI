from abc import ABC, abstractmethod

from invokeai.app.services.style_preset_records.style_preset_records_common import (
    StylePresetChanges,
    StylePresetRecordDTO,
    StylePresetWithoutId,
)


class StylePresetRecordsStorageBase(ABC):
    """Base class for style preset storage services."""

    @abstractmethod
    def get(self, style_preset_id: str) -> StylePresetRecordDTO:
        """Get style preset by id."""
        pass

    @abstractmethod
    def create(self, style_preset: StylePresetWithoutId) -> StylePresetRecordDTO:
        """Creates a style preset."""
        pass

    @abstractmethod
    def update(self, style_preset_id: str, changes: StylePresetChanges) -> StylePresetRecordDTO:
        """Updates a style preset."""
        pass

    @abstractmethod
    def delete(self, style_preset_id: str) -> None:
        """Deletes a style preset."""
        pass

    @abstractmethod
    def get_many(self) -> list[StylePresetRecordDTO]:
        """Gets many workflows."""
        pass
