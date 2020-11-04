from homematicip.base.enums import *
from homematicip.base.functionalChannels import *
from homematicip.device import *
from homematicip.functionalHomes import *
from homematicip.group import *
from homematicip.rule import *
from homematicip.securityEvent import *

TYPE_CLASS_MAP = {
    DeviceType.DEVICE: Device,
    DeviceType.ACCELERATION_SENSOR: AccelerationSensor,
    DeviceType.ALARM_SIREN_INDOOR: AlarmSirenIndoor,
    DeviceType.ALARM_SIREN_OUTDOOR: AlarmSirenOutdoor,
    DeviceType.BLIND_MODULE: BlindModule,
    DeviceType.BRAND_BLIND: BrandBlind,
    DeviceType.BRAND_DIMMER: BrandDimmer,
    DeviceType.BRAND_PUSH_BUTTON: BrandPushButton,
    DeviceType.BRAND_SHUTTER: FullFlushShutter,
    DeviceType.BRAND_SWITCH_MEASURING: BrandSwitchMeasuring,
    DeviceType.BRAND_SWITCH_NOTIFICATION_LIGHT: BrandSwitchNotificationLight,
    DeviceType.BRAND_WALL_MOUNTED_THERMOSTAT: WallMountedThermostatPro,
    DeviceType.FLOOR_TERMINAL_BLOCK_10: FloorTerminalBlock10,
    DeviceType.FLOOR_TERMINAL_BLOCK_12: FloorTerminalBlock12,
    DeviceType.FLOOR_TERMINAL_BLOCK_6: FloorTerminalBlock6,
    DeviceType.FULL_FLUSH_BLIND: FullFlushBlind,
    DeviceType.FULL_FLUSH_CONTACT_INTERFACE: FullFlushContactInterface,
    DeviceType.FULL_FLUSH_DIMMER: FullFlushDimmer,
    DeviceType.FULL_FLUSH_INPUT_SWITCH: FullFlushInputSwitch,
    DeviceType.FULL_FLUSH_SHUTTER: FullFlushShutter,
    DeviceType.FULL_FLUSH_SWITCH_MEASURING: FullFlushSwitchMeasuring,
    DeviceType.HEATING_SWITCH_2: HeatingSwitch2,
    DeviceType.HEATING_THERMOSTAT: HeatingThermostat,
    DeviceType.HEATING_THERMOSTAT_COMPACT: HeatingThermostatCompact,
    DeviceType.HOERMANN_DRIVES_MODULE: HoermannDrivesModule,
    DeviceType.KEY_REMOTE_CONTROL_4: KeyRemoteControl4,
    DeviceType.KEY_REMOTE_CONTROL_ALARM: KeyRemoteControlAlarm,
    DeviceType.LIGHT_SENSOR: LightSensor,
    DeviceType.MOTION_DETECTOR_INDOOR: MotionDetectorIndoor,
    DeviceType.MOTION_DETECTOR_OUTDOOR: MotionDetectorOutdoor,
    DeviceType.MOTION_DETECTOR_PUSH_BUTTON: MotionDetectorPushButton,
    DeviceType.MULTI_IO_BOX: MultiIOBox,
    DeviceType.OPEN_COLLECTOR_8_MODULE: OpenCollector8Module,
    DeviceType.PASSAGE_DETECTOR: PassageDetector,
    DeviceType.PLUGABLE_SWITCH: PlugableSwitch,
    DeviceType.PLUGABLE_SWITCH_MEASURING: PlugableSwitchMeasuring,
    DeviceType.PLUGGABLE_DIMMER: PluggableDimmer,
    DeviceType.PLUGGABLE_MAINS_FAILURE_SURVEILLANCE: PluggableMainsFailureSurveillance,
    DeviceType.PRESENCE_DETECTOR_INDOOR: PresenceDetectorIndoor,
    DeviceType.PRINTED_CIRCUIT_BOARD_SWITCH_2: PrintedCircuitBoardSwitch2,
    DeviceType.PRINTED_CIRCUIT_BOARD_SWITCH_BATTERY: PrintedCircuitBoardSwitchBattery,
    DeviceType.PUSH_BUTTON: PushButton,
    DeviceType.PUSH_BUTTON_6: PushButton6,
    DeviceType.REMOTE_CONTROL_8: RemoteControl8,
    DeviceType.REMOTE_CONTROL_8_MODULE: RemoteControl8Module,
    DeviceType.ROOM_CONTROL_DEVICE: RoomControlDevice,
    DeviceType.ROOM_CONTROL_DEVICE_ANALOG: RoomControlDeviceAnalog,
    DeviceType.ROTARY_HANDLE_SENSOR: RotaryHandleSensor,
    DeviceType.SHUTTER_CONTACT: ShutterContact,
    DeviceType.SHUTTER_CONTACT_INTERFACE: ContactInterface,
    DeviceType.SHUTTER_CONTACT_INVISIBLE: ShutterContact,
    DeviceType.SHUTTER_CONTACT_MAGNETIC: ShutterContactMagnetic,
    DeviceType.SHUTTER_CONTACT_OPTICAL_PLUS: ShutterContactOpticalPlus,
    DeviceType.SMOKE_DETECTOR: SmokeDetector,
    DeviceType.TEMPERATURE_HUMIDITY_SENSOR: TemperatureHumiditySensorWithoutDisplay,
    DeviceType.TEMPERATURE_HUMIDITY_SENSOR_DISPLAY: TemperatureHumiditySensorDisplay,
    DeviceType.TEMPERATURE_HUMIDITY_SENSOR_OUTDOOR: TemperatureHumiditySensorOutdoor,
    DeviceType.TILT_VIBRATION_SENSOR: TiltVibrationSensor,
    DeviceType.TORMATIC_MODULE: GarageDoorModuleTormatic,
    DeviceType.WALL_MOUNTED_THERMOSTAT_PRO: WallMountedThermostatPro,
    DeviceType.WALL_MOUNTED_THERMOSTAT_BASIC_HUMIDITY: WallMountedThermostatBasicHumidity,
    DeviceType.WATER_SENSOR: WaterSensor,
    DeviceType.WEATHER_SENSOR: WeatherSensor,
    DeviceType.WEATHER_SENSOR_PLUS: WeatherSensorPlus,
    DeviceType.WEATHER_SENSOR_PRO: WeatherSensorPro,
    DeviceType.WIRED_DIMMER_3: WiredDimmer3,
    DeviceType.WIRED_INPUT_32: WiredInput32,
    DeviceType.WIRED_SWITCH_8: WiredSwitch8,
}

TYPE_GROUP_MAP = {
    GroupType.GROUP: Group,
    GroupType.ALARM_SWITCHING: AlarmSwitchingGroup,
    GroupType.ENVIRONMENT: EnvironmentGroup,
    GroupType.EXTENDED_LINKED_SHUTTER: ExtendedLinkedShutterGroup,
    GroupType.EXTENDED_LINKED_SWITCHING: ExtendedLinkedSwitchingGroup,
    GroupType.HEATING: HeatingGroup,
    GroupType.HEATING_CHANGEOVER: HeatingChangeoverGroup,
    GroupType.HEATING_COOLING_DEMAND: HeatingCoolingDemandGroup,
    GroupType.HEATING_COOLING_DEMAND_BOILER: HeatingCoolingDemandBoilerGroup,
    GroupType.HEATING_COOLING_DEMAND_PUMP: HeatingCoolingDemandPumpGroup,
    GroupType.HEATING_DEHUMIDIFIER: HeatingDehumidifierGroup,
    GroupType.HEATING_EXTERNAL_CLOCK: HeatingExternalClockGroup,
    GroupType.HEATING_FAILURE_ALERT_RULE_GROUP: HeatingFailureAlertRuleGroup,
    GroupType.HEATING_HUMIDITY_LIMITER: HeatingHumidyLimiterGroup,
    GroupType.HEATING_TEMPERATURE_LIMITER: HeatingTemperatureLimiterGroup,
    GroupType.HOT_WATER: HotWaterGroup,
    GroupType.HUMIDITY_WARNING_RULE_GROUP: HumidityWarningRuleGroup,
    GroupType.INBOX: InboxGroup,
    GroupType.LINKED_SWITCHING: LinkedSwitchingGroup,
    GroupType.LOCK_OUT_PROTECTION_RULE: LockOutProtectionRule,
    GroupType.OVER_HEAT_PROTECTION_RULE: OverHeatProtectionRule,
    GroupType.SECURITY: SecurityGroup,
    GroupType.SECURITY_BACKUP_ALARM_SWITCHING: AlarmSwitchingGroup,
    GroupType.SECURITY_ZONE: SecurityZoneGroup,
    GroupType.SHUTTER_PROFILE: ShutterProfile,
    GroupType.SHUTTER_WIND_PROTECTION_RULE: ShutterWindProtectionRule,
    GroupType.SMOKE_ALARM_DETECTION_RULE: SmokeAlarmDetectionRule,
    GroupType.SWITCHING: SwitchingGroup,
    GroupType.SWITCHING_PROFILE: SwitchingProfileGroup,
}

TYPE_SECURITY_EVENT_MAP = {
    SecurityEventType.ACCESS_POINT_CONNECTED: AccessPointConnectedEvent,
    SecurityEventType.ACCESS_POINT_DISCONNECTED: AccessPointDisconnectedEvent,
    SecurityEventType.ACTIVATION_CHANGED: ActivationChangedEvent,
    SecurityEventType.EXTERNAL_TRIGGERED: ExternalTriggeredEvent,
    SecurityEventType.MAINS_FAILURE_EVENT: MainsFailureEvent,
    SecurityEventType.MOISTURE_DETECTION_EVENT: MoistureDetectionEvent,
    SecurityEventType.OFFLINE_ALARM: OfflineAlarmEvent,
    SecurityEventType.OFFLINE_WATER_DETECTION_EVENT: OfflineWaterDetectionEvent,
    SecurityEventType.SABOTAGE: SabotageEvent,
    SecurityEventType.SENSOR_EVENT: SensorEvent,
    SecurityEventType.SILENCE_CHANGED: SilenceChangedEvent,
    SecurityEventType.SMOKE_ALARM: SmokeAlarmEvent,
    SecurityEventType.WATER_DETECTION_EVENT: WaterDetectionEvent,
}

TYPE_RULE_MAP = {AutomationRuleType.SIMPLE: SimpleRule}

TYPE_FUNCTIONALHOME_MAP = {
    FunctionalHomeType.INDOOR_CLIMATE: IndoorClimateHome,
    FunctionalHomeType.LIGHT_AND_SHADOW: LightAndShadowHome,
    FunctionalHomeType.SECURITY_AND_ALARM: SecurityAndAlarmHome,
    FunctionalHomeType.WEATHER_AND_ENVIRONMENT: WeatherAndEnvironmentHome,
}

TYPE_FUNCTIONALCHANNEL_MAP = {
    FunctionalChannelType.FUNCTIONAL_CHANNEL: FunctionalChannel,
    FunctionalChannelType.ACCELERATION_SENSOR_CHANNEL: AccelerationSensorChannel,
    FunctionalChannelType.ALARM_SIREN_CHANNEL: AlarmSirenChannel,
    FunctionalChannelType.ANALOG_OUTPUT_CHANNEL: AnalogOutputChannel,
    FunctionalChannelType.ANALOG_ROOM_CONTROL_CHANNEL: AnalogRoomControlChannel,
    FunctionalChannelType.BLIND_CHANNEL: BlindChannel,
    FunctionalChannelType.CHANGE_OVER_CHANNEL: ChangeOverChannel,
    FunctionalChannelType.CLIMATE_SENSOR_CHANNEL: ClimateSensorChannel,
    FunctionalChannelType.CONTACT_INTERFACE_CHANNEL: ContactInterfaceChannel,
    FunctionalChannelType.DEHUMIDIFIER_DEMAND_CHANNEL: DehumidifierDemandChannel,
    FunctionalChannelType.DEVICE_BASE: DeviceBaseChannel,
    FunctionalChannelType.DEVICE_BASE_FLOOR_HEATING: DeviceBaseFloorHeatingChannel,
    FunctionalChannelType.DEVICE_GLOBAL_PUMP_CONTROL: DeviceGlobalPumpControlChannel,
    FunctionalChannelType.DEVICE_INCORRECT_POSITIONED: DeviceIncorrectPositionedChannel,
    FunctionalChannelType.DEVICE_OPERATIONLOCK: DeviceOperationLockChannel,
    FunctionalChannelType.DEVICE_PERMANENT_FULL_RX: DevicePermanentFullRxChannel,
    FunctionalChannelType.DEVICE_RECHARGEABLE_WITH_SABOTAGE: DeviceRechargeableWithSabotage,
    FunctionalChannelType.DEVICE_SABOTAGE: DeviceSabotageChannel,
    FunctionalChannelType.DIMMER_CHANNEL: DimmerChannel,
    FunctionalChannelType.DOOR_CHANNEL: DoorChannel,
    FunctionalChannelType.FLOOR_TERMINAL_BLOCK_CHANNEL: FloorTeminalBlockChannel,
    FunctionalChannelType.FLOOR_TERMINAL_BLOCK_LOCAL_PUMP_CHANNEL: FloorTerminalBlockLocalPumpChannel,
    FunctionalChannelType.FLOOR_TERMINAL_BLOCK_MECHANIC_CHANNEL: FloorTerminalBlockMechanicChannel,
    FunctionalChannelType.GENERIC_INPUT_CHANNEL: GenericInputChannel,
    FunctionalChannelType.HEAT_DEMAND_CHANNEL: HeatDemandChannel,
    FunctionalChannelType.HEATING_THERMOSTAT_CHANNEL: HeatingThermostatChannel,
    FunctionalChannelType.INTERNAL_SWITCH_CHANNEL: InternalSwitchChannel,
    FunctionalChannelType.LIGHT_SENSOR_CHANNEL: LightSensorChannel,
    FunctionalChannelType.MAINS_FAILURE_CHANNEL: MainsFailureChannel,
    FunctionalChannelType.MOTION_DETECTION_CHANNEL: MotionDetectionChannel,
    FunctionalChannelType.MULTI_MODE_INPUT_CHANNEL: MultiModeInputChannel,
    FunctionalChannelType.MULTI_MODE_INPUT_SWITCH_CHANNEL: MultiModeInputSwitchChannel,
    FunctionalChannelType.NOTIFICATION_LIGHT_CHANNEL: NotificationLightChannel,
    FunctionalChannelType.PASSAGE_DETECTOR_CHANNEL: PassageDetectorChannel,
    FunctionalChannelType.PRESENCE_DETECTION_CHANNEL: PresenceDetectionChannel,
    FunctionalChannelType.ROTARY_HANDLE_CHANNEL: RotaryHandleChannel,
    FunctionalChannelType.SHADING_CHANNEL: ShadingChannel,
    FunctionalChannelType.SHUTTER_CHANNEL: ShutterChannel,
    FunctionalChannelType.SHUTTER_CONTACT_CHANNEL: ShutterContactChannel,
    FunctionalChannelType.SINGLE_KEY_CHANNEL: SingleKeyChannel,
    FunctionalChannelType.SMOKE_DETECTOR_CHANNEL: SmokeDetectorChannel,
    FunctionalChannelType.SWITCH_CHANNEL: SwitchChannel,
    FunctionalChannelType.SWITCH_MEASURING_CHANNEL: SwitchMeasuringChannel,
    FunctionalChannelType.TILT_VIBRATION_SENSOR_CHANNEL: TiltVibrationSensorChannel,
    FunctionalChannelType.WALL_MOUNTED_THERMOSTAT_PRO_CHANNEL: WallMountedThermostatProChannel,
    FunctionalChannelType.WALL_MOUNTED_THERMOSTAT_WITHOUT_DISPLAY_CHANNEL: WallMountedThermostatWithoutDisplayChannel,
    FunctionalChannelType.WATER_SENSOR_CHANNEL: WaterSensorChannel,
    FunctionalChannelType.WEATHER_SENSOR_CHANNEL: WeatherSensorChannel,
    FunctionalChannelType.WEATHER_SENSOR_PLUS_CHANNEL: WeatherSensorPlusChannel,
    FunctionalChannelType.WEATHER_SENSOR_PRO_CHANNEL: WeatherSensorProChannel,
}
