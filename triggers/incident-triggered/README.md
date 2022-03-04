# splunkoncall-trigger-incident-triggered

This [Splunk On-Call](https://www.splunk.com/en_us/observability/on-call.html) trigger fires when a new incident is created, acknowledged or resolved, depending on the configuration in Splunk On-Call. It uses the Outbound Webhook integration, defined at https://help.victorops.com/knowledge-base/custom-outbound-webhooks.

## Usage and Schema

See the [event.schema.json](https://github.com/relay-integrations/relay-splunkoncall/blob/master/triggers/incident-triggered/event.schema.json) for the formal description of its outputs and the [trigger.yaml](https://github.com/relay-integrations/relay-splunkoncall/blob/master/triggers/incident-triggered/trigger.yaml) for usage examples.

## Example Event Payload

```json
{
    "incident": {
        "incident_id": "12",
        "incident_name": "#12",
        "incident_timestamp": 1646235648962,
        "entity_type": "SERVICE",
        "entity_slug": "",
        "host": "",
        "service": "Incident 12",
        "current_phase": "RESOLVED",
        "annotation_count": 0,
        "alert_count": 1,
        "entity_state": "OK",
        "teams_paged": {
            "0": "team-RBRIvg2KCxZHJF3i"
        },
        "policies_paged": {
            "0": {
                "is_displayable": true,
                "policy": {
                    "name": "Example",
                    "slug": "team-RBRIvg2KCxZHJF3i"
                },
                "team": {
                    "name": "Example",
                    "slug": "team-RBRIvg2KCxZHJF3i"
                },
                "acked_by": "timidri",
                "acked_at": 1646240268298
            }
        },
        "monitor_type": "manual",
        "monitor_name": "vouser-timidri",
        "user": "timidri",
        "first_alert_uuid": "b0d65d74-22f9-4ce3-9f28-70e22042f489",
        "latest_alert_uuid": "b0d65d74-22f9-4ce3-9f28-70e22042f489",
        "tags": {
            "0": "incident12",
            "1": "routingdefault",
            "2": "typesystemmessagenotify",
            "3": "typeincidentnotify"
        },
        "sequencing": {
            "sequence": 428,
            "service_time": 1646240415000
        },
        "room_id": "*",
        "is_multi_responder": false,
        "is_muted": false,
        "entity_display_name": "Incident 12",
        "ack_data": {
            "acks_expected": 0,
            "acks_received": 1,
            "ack_users": {
                "0": "timidri"
            },
            "acks": {
                "0": {
                    "acked_by": "timidri",
                    "acked_at": 1646240268298
                }
            }
        }
    },
    "alert": {
        "hostoutput": "Resolved by timidri",
        "vo_organization_id": "timidri",
        "created_by": "timidri",
        "monitoring_tool": "manual",
        "state_start_time": "1646240268317",
        "timestamp": "1646240268317",
        "vo_uuid": "b0d65d74-22f9-4ce3-9f28-70e22042f489",
        "timet": "1646240415222",
        "entity_display_name": "Incident 12",
        "vo_alert_rcv_time": "1646240415222",
        "message_type": "RECOVERY",
        "alert_type": "RECOVERY",
        "entity_state": "UP",
        "ack_author": "timidri",
        "entity_id": "c7d16822-6eeb-4988-8b04-49942f971559",
        "state_message": "Resolved by timidri",
        "is_vo_ack": "1",
        "monitor_name": "vouser-timidri",
        "notificationtype": "RECOVERY",
        "hoststate": "UP",
        "vo_monitor_type": "28"
    },
    "state": {
        "entity_id": "c7d16822-6eeb-4988-8b04-49942f971559",
        "entity_slug": "vouser-timidri--incident-12",
        "host": "",
        "service": "Incident 12",
        "last_uuid": "b0d65d74-22f9-4ce3-9f28-70e22042f489",
        "current_alert_phase": "RESOLVED",
        "ack_msg": "",
        "ack_user": "timidri",
        "ack_timestamp": 1646240415206,
        "current_state": "OK",
        "state_start_time": 1646235648962,
        "alert_count": 1,
        "last_timestamp": 1646240415206,
        "info_url": "",
        "notificationtype": "",
        "vo_alert_type": "SERVICE",
        "incident_name": "12",
        "incident_timestamp": 1646235648962,
        "monitor_type": "Manual",
        "teams_paged": {
            "0": "team-RBRIvg2KCxZHJF3i"
        },
        "acked_by": "timidri",
        "acked_at": 1646240268298,
        "resolved_by": "timidri",
        "resolved_at": 1646240415206
    }
}
```

## Example Rаw Payload

```json
{
    "INCIDENT.INCIDENT_ID": "9", 
    "INCIDENT.INCIDENT_NAME": "#9", 
    "INCIDENT.INCIDENT_TIMESTAMP": 1646224868334, 
    "INCIDENT.ENTITY_TYPE": "SERVICE", 
    "INCIDENT.ENTITY_SLUG": "", 
    "INCIDENT.HOST": "", 
    "INCIDENT.SERVICE": "Incident 9", 
    "INCIDENT.CURRENT_PHASE": "RESOLVED", 
    "INCIDENT.ANNOTATION_COUNT": 0, 
    "INCIDENT.ALERT_COUNT": 1, 
    "INCIDENT.ENTITY_STATE": "OK", 
    "INCIDENT.TEAMS_PAGED.0": "team-RBRIvg2KCxZHJF3i", 
    "INCIDENT.POLICIES_PAGED.0.IS_DISPLAYABLE": true, 
    "INCIDENT.POLICIES_PAGED.0.POLICY.NAME": "Example", 
    "INCIDENT.POLICIES_PAGED.0.POLICY.SLUG": "team-RBRIvg2KCxZHJF3i", 
    "INCIDENT.POLICIES_PAGED.0.TEAM.NAME": "Example", 
    "INCIDENT.POLICIES_PAGED.0.TEAM.SLUG": "team-RBRIvg2KCxZHJF3i", 
    "INCIDENT.POLICIES_PAGED.0.ACKED_BY": "timidri", 
    "INCIDENT.POLICIES_PAGED.0.ACKED_AT": 1646225112831, 
    "INCIDENT.MONITOR_TYPE": "manual", 
    "INCIDENT.MONITOR_NAME": "vouser-timidri", 
    "INCIDENT.USER": "timidri", 
    "INCIDENT.FIRST_ALERT_UUID": "b27d748f-af4a-4112-a713-44fb6ed16fda", 
    "INCIDENT.LATEST_ALERT_UUID": "b27d748f-af4a-4112-a713-44fb6ed16fda", 
    "INCIDENT.TAGS.0": "incident9", 
    "INCIDENT.TAGS.1": "routingdefault", 
    "INCIDENT.TAGS.2": "typesystemmessagenotify", 
    "INCIDENT.TAGS.3": "typeincidentnotify", 
    "INCIDENT.SEQUENCING.SEQUENCE": 364, 
    "INCIDENT.SEQUENCING.SERVICE_TIME": 1646224868000,
    "INCIDENT.ROOM_ID": "*",
    "INCIDENT.IS_MULTI_RESPONDER": false,
    "INCIDENT.IS_MUTED": false,
    "INCIDENT.ENTITY_DISPLAY_NAME": "Incident 9",
    "INCIDENT.ACK_DATA.ACKS_EXPECTED": 0,
    "INCIDENT.ACK_DATA.ACKS_RECEIVED": 0,
    "ALERT.VO_ORGANIZATION_ID": "timidri",
    "ALERT.created_by": "timidri",
    "ALERT.monitoring_tool": "manual",
    "ALERT.VO_UUID": "b27d748f-af4a-4112-a713-44fb6ed16fda",
    "ALERT.entity_display_name": "Incident 9",
    "ALERT.VO_ALERT_RCV_TIME": "1646224868334",
    "ALERT.message_type": "CRITICAL",
    "ALERT.alert_type": "CRITICAL",
    "ALERT.entity_state": "CRITICAL",
    "ALERT.entity_id": "bae7a0fc-42b6-45cc-9bff-5b1719c96c91",
    "ALERT.state_message": "Incident 9 Body",
    "ALERT.monitor_name": "vouser-timidri",
    "ALERT.VO_MONITOR_TYPE": "28",
    "STATE.ENTITY_ID": "bae7a0fc-42b6-45cc-9bff-5b1719c96c91",
    "STATE.ENTITY_SLUG": "vouser-timidri--incident-9",
    "STATE.HOST": "",
    "STATE.SERVICE": "Incident 9",
    "STATE.LAST_UUID": "b27d748f-af4a-4112-a713-44fb6ed16fda",
    "STATE.CURRENT_ALERT_PHASE": "UNACKED",
    "STATE.ACK_MSG": "",
    "STATE.ACK_USER": "SYSTEM",
    "STATE.ACK_TIMESTAMP": 0,
    "STATE.CURRENT_STATE": "CRITICAL",
    "STATE.STATE_START_TIME": 1646224868334,
    "STATE.ALERT_COUNT": 1,
    "STATE.LAST_TIMESTAMP": 1646224868334,
    "STATE.INFO_URL": "",
    "STATE.NOTIFICATIONTYPE": "",
    "STATE.VO_ALERT_TYPE": "SERVICE",
    "STATE.INCIDENT_NAME": "9",
    "STATE.INCIDENT_TIMESTAMP": 1646224868334,
    "STATE.MONITOR_TYPE": "Manual",
    "STATE.TEAMS_PAGED.0": "team-RBRIvg2KCxZHJF3i",
    "STATE.USERS_PAGED.0": "timidri",
    "STATE.ACKED_BY": null,
    "STATE.ACKED_AT": null,
    "STATE.RESOLVED_BY": null,
    "STATE.RESOLVED_AT": null
}
```
