from marshmallow import Schema, fields, validate


class SessionLogsSchema(Schema):
    uid = fields.String(required=True, validate=validate.Length(min=36, max=36))
    url = fields.String(required=True, validate=validate.Length(min=2, max=255))
    date = fields.Date(required=True)
    time = fields.Time(required=True)


session_schema = SessionLogsSchema(many=True)
