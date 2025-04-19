
'''

# **************************  0x00 - 0x0F  **************************
0x00 Not Used                                                                   **DONE
0x01 Not Used                                                                   **DONE
FUNC_SERIAL_API_GET_INIT_DATA_CMD = 0x02  # serial_api_get_init_data.py         **DONE
FUNC_SERIAL_API_APPL_NODE_INFORMATION_CMD = 0x03  # serial_api_appl_node_information.py    **DONE
FUNC_APPLICATION_COMMAND_HANDLER_CMD = 0x04  # application_command_handler.py   **DONE
FUNC_ZW_GET_CONTROLLER_CAPABILITIES_CMD = 0x05  # zw_get_controller_capabilities.py        **DONE
FUNC_SERIAL_API_SET_TIMEOUTS_CMD = 0x06  # serial_api_set_timeouts.py           **DONE
FUNC_SERIAL_API_GET_CAPABILITIES_CMD = 0x07  # serial_api_get_capabilities.py   **DONE
FUNC_SERIAL_API_SOFT_RESET_CMD = 0x08  # serial_api_soft_reset.py               **DONE
FUNC_ZW_GET_PROTOCOL_VERSION_CMD = 0x09  # zw_get_protocol_version.py           **DONE
FUNC_SERIAL_API_STARTED_CMD = 0x0A  # serial_api_started.py                     **DONE
FUNC_SERIAL_API_SETUP_CMD = 0x0B  # serial_api_setup.py                         **DONE
FUNC_SERIAL_API_APPL_NODE_INFORMATION_CMD_CLASSES_CMD = 0x0C  # serial_api_appl_node_information_cmd_classes.py    **DONE
0x0D Not Used                                                                   **DONE
FUNC_ZW_SEND_DATA_EX_CMD = 0x0E  # zw_send_data_ex.py                           **DONE
FUNC_ZW_SEND_DATA_MULTI_EX_CMD = 0x0F  # zw_send_data_multi_ex.py               **DONE


# **************************  0x10 - 0x1F  **************************
FUNC_ZW_SET_RF_RECEIVE_MODE_CMD = 0x10  # zw_set_rf_receive_mode.py             **DONE
FUNC_ZW_SET_SLEEP_MODE_CMD = 0x11  # zw_set_sleep_mode.py
FUNC_ZW_SEND_NODE_INFORMATION_CMD = 0x12  # zw_send_node_information.py         **DONE
FUNC_ZW_SEND_DATA_CMD = 0x13  # zw_send_data.py                                 **DONE
FUNC_ZW_SEND_DATA_MULTI_CMD = 0x14  # zw_send_data_multi.py                     **DONE
FUNC_ZW_GET_VERSION_CMD = 0x15  # zw_get_version.py                             **DONE
FUNC_ZW_SEND_DATA_ABORT_CMD = 0x16  # zw_send_data_abort.py                     **DONE
FUNC_ZW_RF_POWER_LEVEL_SET_CMD = 0x17  # zw_rf_power_level_set.py               **DONE
FUNC_ZW_SEND_DATA_META_CMD = 0x18  # zw_send_data_meta.py                       **DONE
FUNC_ZW_RESERVED_SD_CMD = 0x19  # zw_reserved_sd.py                             **DONE
FUNC_ZW_RESERVED_SDM_CMD = 0x1A  # zw_reserved_sdm.py                           **DONE
# duplicate *********************************************************
FUNC_ZW_RESERVED_SRI_CMD = 0x1B  # zw_reserved_sri.py                           **DONE
FUNC_ZW_SET_ROUTING_INFO_CMD = 0x1B  # zw_set_routing_info.py
# *******************************************************************
FUNC_ZW_GET_RANDOM_CMD = 0x1C  # zw_get_random.py                               **DONE
FUNC_ZW_RANDOM_CMD = 0x1D  # zw_random.py                                       **DONE
FUNC_SET_RF_POWERLEVEL_REDISCOVERY_CMD = 0x1E  # zw_rf_power_level_rediscovery_set.py    **DONE
0x1F Not Used


# **************************  0x20 - 0x2F  **************************
FUNC_ZW_MEMORY_GET_ID_CMD = 0x20  # memory_get_id.py                            **DONE
FUNC_MEMORY_GET_BYTE_CMD = 0x21  # memory_get_byte.py                           **DONE
FUNC_MEMORY_PUT_BYTE_CMD = 0x22  # memory_put_byte.py                           **DONE
FUNC_MEMORY_GET_BUFFER_CMD = 0x23  # memory_get_buffer.py                       **DONE
FUNC_MEMORY_PUT_BUFFER_CMD = 0x24  # memory_put_buffer.py                       **DONE
FUNC_SERIAL_API_GET_APPL_HOST_MEMORY_OFFSET_CMD = 0x25  # serial_api_get_appl_host_memory_offset.py
FUNC_DEBUG_OUTPUT_CMD = 0x26  # debug_output.py
FUNC_AUTO_PROGRAMMING_CMD = 0x27  # auto_programming.py                         **DONE
FUNC_NVR_GET_VALUE_CMD = 0x28  # nvr_get_value.py                               **DONE
FUNC_NVM_GET_ID_CMD = 0x29  # nvm_get_id.py                                     **DONE
FUNC_NVM_EXT_READ_LONG_BUFFER_CMD = 0x2A  # nvm_ext_read_long_buffer.py         **DONE
FUNC_NVM_EXT_WRITE_LONG_BUFFER_CMD = 0x2B  # nvm_ext_write_long_buffer.py       **DONE
FUNC_NVM_EXT_READ_LONG_BYTE_CMD = 0x2C  # nvm_ext_read_long_byte.py             **DONE
FUNC_NVM_EXT_WRITE_LONG_BYTE_CMD = 0x2D  # nvm_ext_write_long_byte.py           **DONE
FUNC_NVM_BACKUP_RESTORE_CMD = 0x2E  # nvm_backup_restore.py                     **DONE
FUNC_ZW_NVR_GET_APP_VALUE_CMD = 0x2F  # zw_nvr_get_app_value.py                 **DONE


# **************************  0x30 - 0x3F  **************************
FUNC_ZW_CLOCK_SET_CMD = 0x30  # clock_set.py
FUNC_CLOCK_GET_CMD = 0x31  # clock_get.py
FUNC_CLOCK_CMP_CMD = 0x32  # clock_cmp.py
FUNC_RTC_TIMER_CREATE_CMD = 0x33  # rtc_timer_create.py
FUNC_RTC_TIMER_READ_CMD = 0x34  # rtc_timer_read.py
FUNC_RTC_TIMER_DELETE_CMD = 0x35  # rtc_timer_delete.py
FUNC_RTC_TIMER_CALL_CMD = 0x36  # rtc_timer_call.py
FUNC_CLEAR_TX_TIMERS_CMD = 0x37  # clear_tx_timers.py                           **DONE
FUNC_GET_TX_TIMERS_CMD = 0x38  # get_tx_timers.py                               **DONE
FUNC_ZW_CLEAR_NETWORK_STATS_CMD = 0x39  # zw_clear_network_stats.py             **DONE
FUNC_ZW_GET_NETWORK_STATS_CMD = 0x3A  # zw_get_network_stats.py                 **DONE
FUNC_ZW_GET_BACKGROUND_RSSI_CMD = 0x3B  # zw_get_background_rssi.py             **DONE
FUNC_ZW_SET_LISTEN_BEFORE_TALK_THRESHOLD_CMD = 0x3C  # zw_set_listen_before_talk_threshold.py   **DONE
FUNC_NVM_EXT_BACKUP_RESTORE_CMD = 0x3D  # extended_nvm_operations.py
0x3E Not Used                                                                   **DONE
FUNC_ZW_REMOVE_NODE_ID_FROM_NETWORK_CMD = 0x3F  # zw_remove_node_id_from_network.py     **DONE


# **************************  0x40 - 0x4F  **************************
FUNC_ZW_SET_LEARN_NODE_STATE_CMD = 0x40  # zw_set_learn_node_state.py
FUNC_ZW_GET_NODE_PROTOCOL_INFO_CMD = 0x41  # zw_get_node_protocol_info.py       **DONE
FUNC_ZW_SET_DEFAULT_CMD = 0x42  # zw_set_default.py                             **DONE
FUNC_ZW_NEW_CONTROLLER_CMD = 0x43  # zw_new_controller.py
FUNC_ZW_REPLICATION_COMMAND_COMPLETE_CMD = 0x44  # zw_replication_command_complete.py
FUNC_ZW_REPLICATION_SEND_DATA_CMD = 0x45  # zw_replication_send_data.py
FUNC_ZW_ASSIGN_RETURN_ROUTE_CMD = 0x46  # zw_assign_return_route.py             **DONE
FUNC_ZW_DELETE_RETURN_ROUTE_CMD = 0x47  # zw_delete_return_route.py             **DONE
FUNC_ZW_REQUEST_NODE_NEIGHBOR_UPDATE_CMD = 0x48  # zw_request_node_neighbor_update.py **DONE
# duplicate *********************************************************
FUNC_ZW_APPLICATION_CONTROLLER_UPDATE_CMD = 0x49  # zw_application_controller_update.py                            
FUNC_ZW_APPLICATION_UPDATE_CMD = 0x49  # zw_application_update.py               **DONE
# *******************************************************************
FUNC_ZW_ADD_NODE_TO_NETWORK_CMD = 0x4A  # zw_add_node_to_network.py             **DONE
FUNC_ZW_REMOVE_NODE_FROM_NETWORK_CMD = 0x4B  # zw_remove_node_from_network.py   **DONE
FUNC_ZW_CREATE_NEW_PRIMARY_CMD = 0x4C  # zw_create_new_primary.py               **DONE
FUNC_ZW_CONTROLLER_CHANGE_CMD = 0x4D  # zw_controller_change.py                 **DONE
FUNC_ZW_RESERVED_FN_CMD = 0x4E  # zw_reserved_fn.py
FUNC_ZW_ASSIGN_PRIORITY_RETURN_ROUTE_CMD = 0x4F  # zw_assign_priority_return_route.py   **DONE


# **************************  0x50 - 0x5F  **************************
FUNC_ZW_SET_LEARN_MODE_CMD = 0x50  # zw_set_learn_mode.py                       **DONE
FUNC_ZW_ASSIGN_SUC_RETURN_ROUTE_CMD = 0x51  # zw_assign_suc_return_route.py     **DONE
FUNC_ZW_ENABLE_SUC_CMD = 0x52  # zw_enable_suc.py
FUNC_ZW_REQUEST_NETWORK_UPDATE_CMD = 0x53  # zw_request_network_update.py       **DONE
FUNC_ZW_SET_SUC_NODE_ID_CMD = 0x54  # zw_set_suc_node_id.py                     **DONE
FUNC_ZW_DELETE_SUC_RETURN_ROUTE_CMD = 0x55  # zw_delete_suc_return_route.py     **DONE
FUNC_ZW_GET_SUC_NODE_ID_CMD = 0x56  # zw_get_suc_node_id.py                     **DONE
FUNC_ZW_SEND_SUC_ID_CMD = 0x57  # zw_send_suc_node_id.py                        **DONE
FUNC_ZW_ASSIGN_PRIORITY_SUC_RETURN_ROUTE_CMD = 0x58  # zw_assign_priority_suc_return_route.py   **DONE
FUNC_ZW_REDISCOVERY_NEEDED_CMD = 0x59  # zw_rediscovery_needed.py               **DONE
FUNC_ZW_REQUEST_NODE_NEIGHBOR_UPDATE_OPTIONS_CMD = 0x5A  # zw_request_node_neighbor_update_option.py
FUNC_ZW_SUPPORT9600_ONLY_CMD = 0x5B  # zw_support9600_only.py
FUNC_ZW_REQUEST_NEW_ROUTE_DESTINATIONS_CMD = 0x5C  # zw_request_new_route_destinations.py   **DONE
FUNC_ZW_IS_NODE_WITHIN_DIRECT_RANGE_CMD = 0x5D  # zw_is_node_within_direct_range.py   **DONE
FUNC_ZW_EXPLORE_REQUEST_INCLUSION_CMD = 0x5E  # zw_explore_request_inclusion.py **DONE
FUNC_ZW_EXPLORE_REQUEST_EXCLUSION_CMD = 0x5F  # zw_explore_request_exclusion.py **DONE


# **************************  0x60 - 0x6F  **************************
FUNC_ZW_REQUEST_NODE_INFO_CMD = 0x60  # zw_request_node_info.py
FUNC_ZW_REMOVE_FAILED_NODE_ID_CMD = 0x61  # zw_remove_failed_node_id.py
FUNC_ZW_IS_FAILED_NODE_ID_CMD = 0x62  # zw_is_failed_node_id.py
FUNC_ZW_REPLACE_FAILED_NODE_CMD = 0x63  # zw_replace_failed_node.py
0x64 Not Used
FUNC_ZW_SET_ROUTING_MAX_6_00_CMD = 0x65  # zw_set_routing_max_6_00.py
FUNC_ZW_IS_PRIMARY_CTRL_CMD = 0x66  # zw_is_primary_ctrl.py
FUNC_ZW_AES_ECB_CMD = 0x67  # zw_aes_ecb.py
FUNC_ZW_REQUEST_NODETYPE_NEIGHBOR_UPDATE_CMD = 0x68  # zw_request_nodetype_neighbor_update.py
0x69??  FUNC_ID_ZW_TRANSFER_PROTOCOL_CC
0x6A??  FUNC_ID_ZW_ENABLE_NODE_NLS
0x6B??  FUNC_ID_ZW_GET_NODE_NLS_STATE
0x6C??  FUNC_ID_ZW_REQUEST_PROTOCOL_CC_ENCRYPTION
0x6D Not Used
0x6E Not Used
0x6F Not Used


# **************************  0x70 - 0x7F  **************************
FUNC_TIMER_START_CMD = 0x70  # timer_start.py
FUNC_TIMER_RESTART_CMD = 0x71  # timer_restart.py
FUNC_TIMER_CANCEL_CMD = 0x72  # timer_cancel.py
FUNC_TIMER_CALL_CMD = 0x73  # timer_call.py
0x74 Not Used
0x75 Not Used
0x76 Not Used
0x77 Not Used
FUNC_ZW_FIRMWARE_UPDATE_NVM_CMD = 0x78  # zw_firmware_update_nvm.py
0x79 Not Used
0x7A Not Used
0x7B Not Used
0x7C Not Used
0x7D Not Used
0x7E Not Used
0x7F Not Used


# **************************  0x80 - 0x8F  **************************
FUNC_GET_ROUTING_TABLE_LINE_CMD = 0x80  # get_routing_table_line.py                     
FUNC_GET_TX_COUNTER_CMD = 0x81  # get_tx_counter.py                                             
FUNC_RESET_TX_COUNTER_CMD = 0x82  # reset_tx_counter.py                                         
FUNC_STORE_NODEINFO_CMD = 0x83  # store_nodeinfo.py
FUNC_STORE_HOMEID_CMD = 0x84  # store_homeid.py
0x85 Not Used
0x86 Not Used
0x87 Not Used
0x88 Not Used
0x89 Not Used
0x8A Not Used
0x8B Not Used
0x8C Not Used
0x8D Not Used
0x8E Not Used
0x8F Not Used


# **************************  0x90 - 0x9F  **************************
FUNC_LOCK_ROUTE_RESPONSE_CMD = 0x90  # lock_unlock_last_route.py
0x91 Not Used
# duplicate *********************************************************
FUNC_ZW_GET_LAST_WORKING_ROUTE_CMD = 0x92  # zw_get_last_working_route.py
FUNC_ZW_GET_PRIORITY_ROUTE_CMD = 0x92  # zw_get_priority_route.py
# *******************************************************************
# duplicate *********************************************************
FUNC_ZW_SET_LAST_WORKING_ROUTE_CMD = 0x93  # zw_set_last_working_route.py
FUNC_ZW_SET_PRIORITY_ROUTE_CMD = 0x93  # zw_set_priority_route.py
# *******************************************************************
0x94 Not Used
FUNC_SERIAL_API_TEST_CMD = 0x95  # serial_api_test.py
0x96 Not Used
0x97 Not Used
FUNC_SERIAL_API_EXT_CMD = 0x98  # serial_api_ext.py
0x99 Not Used
0x9A Not Used
0x9B Not Used
FUNC_ZW_SECURITY_SETUP_CMD = 0x9C  # zw_security_setup.py
FUNC_APPLICATION_SECURITY_EVENT_CMD = 0x9D  # application_security_event.py
0x9E Not Used
0x9F Not Used

# **************************  0xA0 - 0xAF  **************************
FUNC_SERIAL_API_APPL_SLAVE_NODE_INFORMATION_CMD = 0xA0  # serial_api_appl_slave_node_information.py
FUNC_APPLICATION_SLAVE_COMMAND_HANDLER_CMD = 0xA1  # application_slave_command_handler.py
FUNC_ZW_SEND_SLAVE_NODE_INFORMATION_CMD = 0xA2  # zw_send_slave_node_information.py
FUNC_ZW_SEND_SLAVE_DATA_CMD = 0xA3  # zw_send_slave_data.py
FUNC_ZW_SET_SLAVE_LEARN_MODE_CMD = 0xA4  # zw_set_slave_learn_mode.py
FUNC_ZW_GET_VIRTUAL_NODES_CMD = 0xA5  # zw_get_virtual_nodes.py
FUNC_ZW_IS_VIRTUAL_NODE_CMD = 0xA6  # zw_is_virtual_node.py
FUNC_ZW_RESERVED_SSD_CMD = 0xA7  # zw_reserved_ssd.py
FUNC_APPLICATION_COMMAND_HANDLER_BRIDGE_CMD = 0xA8  # application_command_handler_bridge.py
FUNC_ZW_SEND_DATA_BRIDGE_CMD = 0xA9  # zw_send_data_bridge.py
FUNC_ZW_SEND_DATA_META_BRIDGE_CMD = 0xAA  # zw_send_data_meta_bridge.py
FUNC_ZW_SEND_DATA_MULTI_BRIDGE_CMD = 0xAB  # zw_send_data_multi_bridge.py       **DONE
0xAC         FUNC_ID_ZW_SEND_PROTOCOL_DATA
0xAD Not Used
0xAE Not Used
0xAF Not Used


# **************************  0xB0 - 0xBF  **************************
FUNC_PWR_SETSTOPMODE_CMD = 0xB0  # pwr_set_stop_mode.py
FUNC_PWR_CLK_PD_CMD = 0xB1  # pwr_clk_pd.py
FUNC_PWR_CLK_PUP_CMD = 0xB2  # pwr_clk_pup.py
FUNC_PWR_SELECT_CLK_CMD = 0xB3  # pwr_select_clk.py
FUNC_ZW_SET_WUT_TIMEOUT_CMD = 0xB4  # zw_set_wut_timeout.py                     **DONE
FUNC_ZW_IS_WUT_KICKED_CMD = 0xB5  # zw_is_wut_kicked.py
FUNC_ZW_WATCHDOG_ENABLE_CMD = 0xB6  # zw_watchdog_enable.py                     **DONE
FUNC_ZW_WATCHDOG_DISABLE_CMD = 0xB7  # zw_watchdog_disable.py                   **DONE
FUNC_ZW_WATCHDOG_KICK_CMD = 0xB8  # zw_watchdog_kick.py                         **DONE
# duplicate *********************************************************
FUNC_ZW_INT_EXT_LEVEL_SET_CMD = 0xB9  # zw_int_ext_level_set.py
FUNC_ZW_SET_EXT_INT_LEVEL_CMD = 0xB9  # zw_set_ext_int_level.py                 **DONE
# *******************************************************************
FUNC_ZW_RF_POWER_LEVEL_GET_CMD = 0xBA  # zw_rf_power_level_get.py               **DONE
FUNC_ZW_GET_NEIGHBOR_COUNT_CMD = 0xBB  # zw_get_neighbor_count.py               **DONE
FUNC_ZW_ARE_NODES_NEIGHBORS_CMD = 0xBC  # zw_are_nodes_neighbours.py            **DONE
FUNC_ZW_TYPE_LIBRARY_CMD = 0xBD  # zw_type_library.py                           **DONE
FUNC_ZW_SEND_TEST_FRAME_CMD = 0xBE  # zw_send_test_frame.py                     **DONE
FUNC_ZW_GET_PROTOCOL_STATUS_CMD = 0xBF  # zw_get_protocol_status.py             **DONE


# **************************  0xC0 - 0xCF  **************************
0xC0 Not Used
0xC1 Not Used
0xC2 Not Used
0xC3 Not Used
0xC4 Not Used
0xC5 Not Used
0xC6 Not Used
0xC7 Not Used
0xC8 Not Used
0xC9 Not Used
0xCA Not Used
0xCB Not Used
0xCC Not Used
0xCD Not Used
0xCE Not Used
0xCF Not Used


# **************************  0xD0 - 0xDF  **************************
FUNC_ZW_SET_PROMISCUOUS_MODE_CMD = 0xD0  # zw_set_promiscuous_mode.py           **DONE
FUNC_PROMISCUOUS_APPLICATION_COMMAND_HANDLER_CMD = 0xD1  # promiscuous_application_command_handler.py
FUNC_ZW_WATCHDOG_START_CMD = 0xD2  # zw_watchdog_start.py                       **DONE
FUNC_ZW_WATCHDOG_STOP_CMD = 0xD3  # zw_watchdog_stop.py                         **DONE
FUNC_ZW_SET_ROUTING_MAX_CMD = 0xD4  # zw_set_routing_max.py                     **DONE
FUNC_ZW_GET_ROUTING_MAX_CMD = 0xD5  # zw_get_routing_max.py                     **DONE
FUNC_ZW_NETWORK_MANAGEMENT_SET_MAX_INCLUSION_REQUEST_INTERVALS_CMD = 0xD6  # zw_network_management_set_max_inclusion_request_intervals.py    **DONE
FUNC_PM_STAY_AWAKE_CMD = 0xD7  # pm_stay_awake.py
FUNC_PM_CANCEL_CMD = 0xD8  # pm_cancel.py
FUNC_ZW_INITIATE_SHUTDOWN_CMD = 0xD9  # zw_initiate_shutdown.py
FUNC_SERIAL_API_GET_LR_NODES_CMD = 0xDA  # serial_api_get_lr_nodes.py           **DONE
FUNC_GET_LR_CHANNEL_CMD = 0xDB  # get_lr_channel.py                             **DONE
FUNC_SET_LR_CHANNEL_CMD = 0xDC  # set_lr_channel.py                             **DONE
FUNC_ZW_SET_LR_VIRTUAL_IDS_CMD = 0xDD  # zw_set_lr_virtual_ids.py               **DONE
FUNC_GET_DCDC_CONFIG_CMD = 0xDE  # get_dcdc_config.py                           **DONE
FUNC_SET_DCDC_CONFIG_CMD = 0xDF  # set_dcdc_config.py                           **DONE


# **************************  0xE0 - 0xEF  **************************
ZwNunitCmd = 0xE0  # zw_nunit_cmd.py
FUNC_ZW_NUNIT_INIT_CMD = 0xE1  # zw_nunit_init.py
ZwNunitList = 0xE2  # zw_nunit_list.py                                          FUNC_ZW_NUNIT_LIST_CMD
FUNC_ZW_NUNIT_RUN_CMD = 0xE3  # zw_nunit_run.py
FUNC_ZW_NUNIT_END_CMD = 0xE4  # zw_nunit_end.py
0xE5 Not Used
0xE6 Not Used
FUNC_ENABLE_RADIO_PTI_CMD = 0xE7  # enable_radio_pti.py
FUNC_GET_RADIO_PTI_CMD = 0xE8  # get_radio_pti.py
FUNC_SEND_NOP_CMD = 0xE9  # send_nop.py                                         **DONE
0xEA Not Used
0xEB Not Used
0xEC Not Used
0xED Not Used
FUNC_SERIAL_API_POWER_MANAGEMENT_CMD = 0xEE  # serial_api_power_management.py   **DONE
FUNC_SERIAL_API_READY_CMD = 0xEF  # serial_api_ready.py                         **DONE


# **************************  0xF0 - 0xFF  **************************
FUNC_PROPRIETARY_0_CMD = 0xF0  # proprietary_0.py
FUNC_PROPRIETARY_1_CMD = 0xF1  # proprietary_1.py
FUNC_PROPRIETARY_2_CMD = 0xF2  # proprietary_2.py
FUNC_PROPRIETARY_3_CMD = 0xF3  # proprietary_3.py
FUNC_PROPRIETARY_4_CMD = 0xF4  # proprietary_4.py
FUNC_PROPRIETARY_5_CMD = 0xF5  # proprietary_5.py
FUNC_PROPRIETARY_6_CMD = 0xF6  # proprietary_6.py
FUNC_PROPRIETARY_7_CMD = 0xF7  # proprietary_7.py
FUNC_PROPRIETARY_8_CMD = 0xF8  # proprietary_8.py
FUNC_PROPRIETARY_9_CMD = 0xF9  # proprietary_9.py
FUNC_PROPRIETARY_A_CMD = 0xFA  # proprietary_a.py
FUNC_PROPRIETARY_B_CMD = 0xFB  # proprietary_b.py
FUNC_PROPRIETARY_C_CMD = 0xFC  # proprietary_c.py
FUNC_PROPRIETARY_D_CMD = 0xFD  # proprietary_d.py
FUNC_PROPRIETARY_E_CMD = 0xFE  # proprietary_e.py
FUNC_UNKNOWN_CMD = 0xFF  # unknown.py


'''

import ctypes

# Max theoretical Z-Wave frame payload size in a Z-Wave protocol using 3CH network
# The real Z-Wave frame payload type depends on various parameters (routed, multicast, explore, security and/or number of RF channels)
# Customer must not use this value in their application. They must use the value MaxPayloadSize from the SNetworkInfo structure.
ZW_MAX_PAYLOAD_SIZE = 160

# Numbers of nodes we can support when sending multicast frames on LR channel
MULTICAST_NODE_LIST_SIZE = 64

TX_BUFFER_SIZE = 170

MAX_NODE_INFO_LENGTH = 159

uint8_t = ctypes.c_uint8
uint16_t = ctypes.c_uint16
uint32_t = ctypes.c_uint32


FRAME_TYPE_REQUEST = 0x00
FRAME_TYPE_RESPONSE = 0x01
FRAME_TYPE_CALLBACK = 0x04
FRAME_TYPE_UNSOLICITED = 0x08
FRAME_TYPE_ACK = 0x80


ACK = 0x06
NAK = 0x15
CAN = 0x18
SOF = 0x01


REQUEST_FRAMES = []
RESPONSE_FRAMES = []
CALLBACK_FRAMES = []
UNSOLICITED_FRAMES = []


class ZwaveException(Exception):
    pass


class FrameError(ZwaveException):
    pass


class _FrameMeta(type(ctypes.Structure)):
    frame_type = 0x00
    id = 0x00

    def __eq__(cls, other):  # NOQA
        if isinstance(other, int):
            return cls.id == other
        elif isinstance(other, DATA_FRAME):
            return super().__eq__(other.__class__)

        return False

    def __ne__(cls, other):  # NOQA
        return not cls.__eq__(other)

    def __init__(cls, name, bases, dct):  # NOQA
        super().__init__(name, bases, dct)

        if cls.frame_type & FRAME_TYPE_RESPONSE:
            RESPONSE_FRAMES.append(cls)
        elif cls.frame_type & FRAME_TYPE_CALLBACK:
            CALLBACK_FRAMES.append(cls)
        elif cls.frame_type & FRAME_TYPE_UNSOLICITED:
            UNSOLICITED_FRAMES.append(cls)
        else:
            REQUEST_FRAMES.append(cls)

    def __call__(cls, *args, **kwargs):
        print(args, kwargs)
        return super().__call__(*args, **kwargs)


class NODE_ID_8_FRAME(ctypes.Structure):
    _fields_ = [('node_id', uint8_t)]


class NODE_ID_16_FRAME(ctypes.Structure):
    _fields_ = [('node_id', uint16_t)]


class NODE_ID_FIELDS(ctypes.Union):
    _fields_ = []


class DATA_FRAME(ctypes.Structure, metaclass=_FrameMeta):
    id = 0x00
    frame_type = FRAME_TYPE_UNSOLICITED
    _node_id_len = 1

    _fields_ = [
        ('_sof', uint8_t),
        ('_length', uint8_t),
        ('_frame_type', uint8_t),
        ('_command_id', uint8_t),
    ]

    @property
    def _fields(self) -> NODE_ID_8_FRAME | NODE_ID_16_FRAME:
        if self._node_id_len == 1:
            return self._node_id_8
        else:
            return self._node_id_16

    @property
    def node_id_len(self):
        return self._node_id_len

    @node_id_len.setter
    def node_id_len(self, value):
        self._node_id_len = value

    @property
    def packet_length(self):
        raise NotImplementedError

    @classmethod
    def from_bytes(cls, data: bytearray):  # NOQA
        frame_type, length, type_, command_id = data[:4]

        if frame_type & FRAME_TYPE_RESPONSE:
            if command_id in RESPONSE_FRAMES:
                index = RESPONSE_FRAMES.index(command_id)
                frame_cls = RESPONSE_FRAMES[index]
            else:
                raise FrameError
        elif frame_type & FRAME_TYPE_REQUEST:
            if command_id in UNSOLICITED_FRAMES:
                index = UNSOLICITED_FRAMES.index(command_id)
                frame_cls = UNSOLICITED_FRAMES[index]
            elif command_id in CALLBACK_FRAMES:
                index = CALLBACK_FRAMES.index(command_id)
                frame_cls = CALLBACK_FRAMES[index]
            else:
                raise FrameError
        else:
            raise FrameError

        self = frame_cls.from_buffer_copy(data)
        return self

    def to_bytes(self) -> bytearray:
        self._sof = 0x01  # noqa
        if self.frame_type & FRAME_TYPE_RESPONSE:
            self._frame_type = FRAME_TYPE_RESPONSE  # NOQA

        self._length = self.payload_length + 3  # NOQA
        self.__command_id = self.id  # NOQA
        data = bytearray(self)[:self._length + 1]

        checksum = 0xFF
        for item in data[1:]:
            checksum ^ item
        data += bytearray([checksum])

        return data


SOF_TIMEOUT = 1500  # milliseconds

def rx(serial):
    data = bytearray()

    ACK = 0x06
    NAK = 0x15
    CAN = 0x18
    SOF = 0x01

    byte = serial.rx_byte()

    if byte is None:
        return None

    if byte == 0x01:
        data = bytearray([0x01])

        length = None
        while length is None:
            length = serial.rx_byte()

        data += bytearray([length])
        data += bytearray(serial.rx_bytes(length - 1, SOF_TIMEOUT))

        if len(data) - 1 != length:
            return None

        checksum = 0xFF
        for item in data[1:]:
            checksum ^= item

        if checksum != data[-1]:
            return NAK

        return DATA_FRAME.from_bytes(data[:-1])

    return byte


def send_frame(serial, frame: bytearray):
    serial.tx_bytes(frame)

