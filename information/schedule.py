from typing import Optional

from pydantic import BaseModel


class Attendance(BaseModel):
    attendance_reason: Optional[str]


class Subject(BaseModel):
    subject_name: str
    subject_name_eng: Optional[str]


class Group(BaseModel):
    group_name: str
    subject: Subject


class Room(BaseModel):
    room_name: str
    room_description: str


class WorkList(BaseModel):
    work_comment: Optional[str]
    work_criterion: Optional[str]
    work_form: int


class LessonsList(BaseModel):
    lesson_canvas: int
    lesson_url: Optional[str]
    lesson_hw: Optional[str]
    lesson_hw_date: Optional[str]
    lesson_hw_url: Optional[str]
    lesson_comment: Optional[str]
    attendance: list[Attendance]


class ZoomMeetings(BaseModel):

    meeting_url: str


class SchedulesList(BaseModel):
    shedule_room: int
    lessons: list[LessonsList]
    zoom_meetings: Optional[ZoomMeetings]
    group: Group
    room: Room


class DataList(BaseModel):
    period_num_day: int
    period_name: str
    period_start: str
    period_end: str
    date: str
    schedules: list[SchedulesList]


class ScheduleResponse(BaseModel):
    data: list[DataList]