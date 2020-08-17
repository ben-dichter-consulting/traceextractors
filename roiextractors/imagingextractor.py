from abc import ABC, abstractmethod
import numpy as np
from spikeextractors.baseextractor import BaseExtractor
from .extraction_tools import ArrayType, PathType, NumpyArray, DtypeType


class ImagingExtractor(ABC, BaseExtractor):
    """An abstract class that contains all the meta-data and input data from
       the imaging data.
    """
    def __init__(self):
        BaseExtractor.__init__(self)
        self._memmapped = False

    @abstractmethod
    def get_frames(self, frame_idxs: ArrayType, channel: int = 0) -> NumpyArray:
        pass

    @abstractmethod
    def get_video(self, start_frame: int = None, end_frame: int = None, channel: int = 0) -> NumpyArray:
        pass

    @abstractmethod
    def get_image_size(self) -> ArrayType:
        pass

    @abstractmethod
    def get_num_frames(self) -> int:
        pass

    @abstractmethod
    def get_sampling_frequency(self) -> float:
        pass

    @abstractmethod
    def get_channel_names(self) -> list:
        """List of  channels in the recoding.

        Returns
        -------
        channel_names: list
            List of strings of channel names
        """
        pass

    @abstractmethod
    def get_num_channels(self) -> int:
        """Total number of active channels in the recording

        Returns
        -------
        no_of_channels: int
            integer count of number of channels
        """
        pass

    def get_dtype(self) -> DtypeType:
        return self.get_frame(0, 0).dtype

    def frame_to_time(self, frame: int):
        '''This function converts a user-inputted frame index to a time with units of seconds.

        Parameters
        ----------
        frame: float
            The frame to be converted to a time

        Returns
        -------
        time: float
            The corresponding time in seconds
        '''
        # Default implementation
        return frame / self.get_sampling_frequency()

    def time_to_frame(self, time):
        '''This function converts a user-inputted time (in seconds) to a frame index.

        Parameters
        -------
        time: float
            The time (in seconds) to be converted to frame index

        Returns
        -------
        frame: float
            The corresponding frame index
        '''
        # Default implementation
        return time * self.get_sampling_frequency()

    @staticmethod
    def write_imaging(imaging, save_path: PathType):
        """
        Static method to write imaging.

        Parameters
        ----------
        imaging: ImagingExtractor object
            The EXTRACT segmentation object from which an EXTRACT native format
            file has to be generated.
        save_path: str
            path to save the native format.
        """
        raise NotImplementedError


