# Copyright 2014 The Crashpad Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
  'includes': [
    '../build/crashpad.gypi',
  ],
  'targets': [
    {
      'target_name': 'crashpad_util',
      'type': 'static_library',
      'dependencies': [
        '../compat/compat.gyp:crashpad_compat',
        '../third_party/mini_chromium/mini_chromium.gyp:base',
        '../third_party/zlib/zlib.gyp:zlib',
        '../third_party/lss/lss.gyp:lss',
      ],
      'defines': [ 'ZLIB_CONST' ],
      'include_dirs': [
        '..',
        '<(INTERMEDIATE_DIR)',
      ],
      'sources': [
        'file/delimited_file_reader.cc',
        'file/delimited_file_reader.h',
        'file/directory_reader.h',
        'file/directory_reader_posix.cc',
        'file/directory_reader_win.cc',
        'file/file_helper.cc',
        'file/file_helper.h',
        'file/file_io.cc',
        'file/file_io.h',
        'file/file_io_posix.cc',
        'file/file_io_win.cc',
        'file/file_reader.cc',
        'file/file_reader.h',
        'file/file_seeker.cc',
        'file/file_seeker.h',
        'file/filesystem.h',
        'file/filesystem_posix.cc',
        'file/filesystem_win.cc',
        'file/file_writer.cc',
        'file/file_writer.h',
        'file/output_stream_file_writer.cc',
        'file/output_stream_file_writer.h',
        'file/scoped_remove_file.cc',
        'file/scoped_remove_file.h',
        'file/string_file.cc',
        'file/string_file.h',
        'linux/address_types.h',
        'linux/auxiliary_vector.cc',
        'linux/auxiliary_vector.h',
        'linux/checked_address_range.h',
        'linux/direct_ptrace_connection.cc',
        'linux/direct_ptrace_connection.h',
        'linux/exception_handler_client.cc',
        'linux/exception_handler_client.h',
        'linux/exception_handler_protocol.cc',
        'linux/exception_handler_protocol.h',
        'linux/exception_information.h',
        'linux/initial_signal_dispositions.cc',
        'linux/initial_signal_dispositions.h',
        'linux/memory_map.cc',
        'linux/memory_map.h',
        'linux/proc_stat_reader.cc',
        'linux/proc_stat_reader.h',
        'linux/proc_task_reader.cc',
        'linux/proc_task_reader.h',
        'linux/ptrace_broker.cc',
        'linux/ptrace_broker.h',
        'linux/ptrace_client.cc',
        'linux/ptrace_client.h'
        'linux/ptrace_connection.h',
        'linux/ptracer.cc',
        'linux/ptracer.h',
        'linux/scoped_pr_set_dumpable.cc',
        'linux/scoped_pr_set_dumpable.h',
        'linux/scoped_pr_set_ptracer.cc',
        'linux/scoped_pr_set_ptracer.h',
        'linux/scoped_ptrace_attach.cc',
        'linux/scoped_ptrace_attach.h',
        'linux/socket.cc',
        'linux/socket.h',
        'linux/thread_info.cc',
        'linux/thread_info.h',
        'linux/traits.h',
        'mac/checked_mach_address_range.h',
        'mac/launchd.h',
        'mac/launchd.mm',
        'mac/mac_util.cc',
        'mac/mac_util.h',
        'mac/service_management.cc',
        'mac/service_management.h',
        'mac/sysctl.cc',
        'mac/sysctl.h',
        'mac/xattr.cc',
        'mac/xattr.h',
        'mach/child_port.defs',
        'mach/child_port_handshake.cc',
        'mach/child_port_handshake.h',
        'mach/child_port_server.cc',
        'mach/child_port_server.h',
        'mach/child_port_types.h',
        'mach/composite_mach_message_server.cc',
        'mach/composite_mach_message_server.h',
        'mach/exc_client_variants.cc',
        'mach/exc_client_variants.h',
        'mach/exc_server_variants.cc',
        'mach/exc_server_variants.h',
        'mach/exception_behaviors.cc',
        'mach/exception_behaviors.h',
        'mach/exception_ports.cc',
        'mach/exception_ports.h',
        'mach/exception_types.cc',
        'mach/exception_types.h',
        'mach/mach_extensions.cc',
        'mach/mach_extensions.h',
        'mach/mach_message.cc',
        'mach/mach_message.h',
        'mach/mach_message_server.cc',
        'mach/mach_message_server.h',
        'mach/notify_server.cc',
        'mach/notify_server.h',
        'mach/scoped_task_suspend.cc',
        'mach/scoped_task_suspend.h',
        'mach/symbolic_constants_mach.cc',
        'mach/symbolic_constants_mach.h',
        'mach/task_for_pid.cc',
        'mach/task_for_pid.h',
        'misc/address_sanitizer.h',
        'misc/address_types.h',
        'misc/arraysize.h',
        'misc/as_underlying_type.h',
        'misc/capture_context.h',
        'misc/capture_context_linux.S',
        'misc/capture_context_mac.S',
        'misc/capture_context_win.asm',
        'misc/clock.h',
        'misc/clock_mac.cc',
        'misc/clock_posix.cc',
        'misc/clock_win.cc',
        'misc/elf_note_types.h',
        'misc/from_pointer_cast.h',
        'misc/implicit_cast.h',
        'misc/initialization_state.h',
        'misc/initialization_state_dcheck.cc',
        'misc/initialization_state_dcheck.h',
        'misc/lexing.cc',
        'misc/lexing.h',
        'misc/metrics.cc',
        'misc/metrics.h',
        'misc/paths.h',
        'misc/paths_mac.cc',
        'misc/paths_linux.cc',
        'misc/paths_win.cc',
        'misc/pdb_structures.cc',
        'misc/pdb_structures.h',
        'misc/random_string.cc',
        'misc/random_string.h',
        'misc/range_set.cc',
        'misc/range_set.h',
        'misc/reinterpret_bytes.cc',
        'misc/reinterpret_bytes.h',
        'misc/scoped_forbid_return.cc',
        'misc/scoped_forbid_return.h',
        'misc/symbolic_constants_common.h',
        'misc/time.cc',
        'misc/time.h',
        'misc/time_linux.cc',
        'misc/time_win.cc',
        'misc/tri_state.h',
        'misc/uuid.cc',
        'misc/uuid.h',
        'misc/zlib.cc',
        'misc/zlib.h',
        'net/http_body.cc',
        'net/http_body.h',
        'net/http_body_gzip.cc',
        'net/http_body_gzip.h',
        'net/http_headers.h',
        'net/http_multipart_builder.cc',
        'net/http_multipart_builder.h',
        'net/http_transport.cc',
        'net/http_transport.h',
        'net/http_transport_mac.mm',
        'net/http_transport_win.cc',
        'net/url.cc',
        'net/url.h',
        'numeric/checked_address_range.cc',
        'numeric/checked_address_range.h',
        'numeric/checked_range.h',
        'numeric/checked_vm_address_range.h',
        'numeric/in_range_cast.h',
        'numeric/int128.h',
        'numeric/safe_assignment.h',
        'posix/close_multiple.cc',
        'posix/close_multiple.h',
        'posix/close_stdio.cc',
        'posix/close_stdio.h',
        'posix/drop_privileges.cc',
        'posix/drop_privileges.h',
        'posix/double_fork_and_exec.cc',
        'posix/double_fork_and_exec.h',
        'posix/process_info.h',
        'posix/process_info_linux.cc',
        'posix/process_info_mac.cc',
        'posix/scoped_dir.cc',
        'posix/scoped_dir.h',
        'posix/scoped_mmap.cc',
        'posix/scoped_mmap.h',
        'posix/signals.cc',
        'posix/signals.h',
        'posix/symbolic_constants_posix.cc',
        'posix/symbolic_constants_posix.h',
        'process/process_id.h',
        'process/process_memory.cc',
        'process/process_memory.h',
        'process/process_memory_linux.cc',
        'process/process_memory_linux.h',
        'process/process_memory_mac.cc',
        'process/process_memory_mac.h',
        'process/process_memory_native.h',
        'process/process_memory_range.cc',
        'process/process_memory_range.h',
        'stdlib/aligned_allocator.cc',
        'stdlib/aligned_allocator.h',
        'stdlib/map_insert.h',
        'stdlib/objc.h',
        'stdlib/string_number_conversion.cc',
        'stdlib/string_number_conversion.h',
        'stdlib/strlcpy.cc',
        'stdlib/strlcpy.h',
        'stdlib/strnlen.cc',
        'stdlib/strnlen.h',
        'stdlib/thread_safe_vector.h',
        'stream/base94_output_stream.cc',
        'stream/base94_output_stream.h',
        'stream/file_encoder.cc',
        'stream/file_encoder.h',
        'stream/file_output_stream.cc',
        'stream/file_output_stream.h',
        'stream/log_output_stream.cc',
        'stream/log_output_stream.h',
        'stream/output_stream_interface.h',
        'stream/zlib_output_stream.cc',
        'stream/zlib_output_stream.h',
        'string/split_string.cc',
        'string/split_string.h',
        'synchronization/semaphore_mac.cc',
        'synchronization/semaphore_posix.cc',
        'synchronization/semaphore_win.cc',
        'synchronization/semaphore.h',
        'thread/stoppable.h',
        'thread/thread.cc',
        'thread/thread.h',
        'thread/thread_log_messages.cc',
        'thread/thread_log_messages.h',
        'thread/thread_posix.cc',
        'thread/thread_win.cc',
        'thread/worker_thread.cc',
        'thread/worker_thread.h',
        'win/address_types.h',
        'win/checked_win_address_range.h',
        'win/command_line.cc',
        'win/command_line.h',
        'win/context_wrappers.h',
        'win/critical_section_with_debug_info.cc',
        'win/critical_section_with_debug_info.h',
        'win/exception_handler_server.cc',
        'win/exception_handler_server.h',
        'win/get_function.cc',
        'win/get_function.h',
        'win/get_module_information.cc',
        'win/get_module_information.h',
        'win/handle.cc',
        'win/handle.h',
        'win/initial_client_data.cc',
        'win/initial_client_data.h',
        'win/module_version.cc',
        'win/module_version.h',
        'win/nt_internals.cc',
        'win/nt_internals.h',
        'win/ntstatus_logging.cc',
        'win/ntstatus_logging.h',
        'win/process_info.cc',
        'win/process_info.h',
        'win/process_structs.h',
        'win/registration_protocol_win.cc',
        'win/registration_protocol_win.h',
        'win/safe_terminate_process.asm',
        'win/safe_terminate_process.h',
        'win/scoped_handle.cc',
        'win/scoped_handle.h',
        'win/scoped_local_alloc.cc',
        'win/scoped_local_alloc.h',
        'win/scoped_process_suspend.cc',
        'win/scoped_process_suspend.h',
        'win/scoped_set_event.cc',
        'win/scoped_set_event.h',
        'win/session_end_watcher.cc',
        'win/session_end_watcher.h',
        'win/termination_codes.h',
        'win/xp_compat.h',
      ],
      'conditions': [
        ['OS=="mac"', {
          'conditions': [
            ['GENERATOR=="ninja"', {
              # ninja’s rules can’t deal with sources that have paths relative
              # to environment variables like SDKROOT. Copy the .defs files out
              # of SDKROOT and into a place they can be referenced without any
              # environment variables.
              'copies': [
                {
                  'destination': '<(INTERMEDIATE_DIR)/util/mach',
                  'files': [
                    '$(SDKROOT)/usr/include/mach/exc.defs',
                    '$(SDKROOT)/usr/include/mach/mach_exc.defs',
                    '$(SDKROOT)/usr/include/mach/notify.defs',
                  ],
                },
              ],
              'sources': [
                '<(INTERMEDIATE_DIR)/util/mach/exc.defs',
                '<(INTERMEDIATE_DIR)/util/mach/mach_exc.defs',
                '<(INTERMEDIATE_DIR)/util/mach/notify.defs',
              ],
            }, {  # else: GENERATOR!="ninja"
              # The Xcode generator does copies after rules, so the above trick
              # won’t work, but its rules tolerate sources with SDKROOT-relative
              # paths.
              'sources': [
                '$(SDKROOT)/usr/include/mach/exc.defs',
                '$(SDKROOT)/usr/include/mach/mach_exc.defs',
                '$(SDKROOT)/usr/include/mach/notify.defs',
              ],
            }],
          ],
          'rules': [
            {
              'rule_name': 'mig',
              'extension': 'defs',
              'inputs': [
                'mach/mig.py',
              ],
              'outputs': [
                '<(INTERMEDIATE_DIR)/util/mach/<(RULE_INPUT_ROOT)User.c',
                '<(INTERMEDIATE_DIR)/util/mach/<(RULE_INPUT_ROOT)Server.c',
                '<(INTERMEDIATE_DIR)/util/mach/<(RULE_INPUT_ROOT).h',
                '<(INTERMEDIATE_DIR)/util/mach/<(RULE_INPUT_ROOT)Server.h',
              ],
              'action': [
                'python',
                '<@(_inputs)',
                '<(RULE_INPUT_PATH)',
                '<@(_outputs)',
                '--include=../compat/mac'
              ],
              'process_outputs_as_sources': 1,
            },
          ],
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/CoreFoundation.framework',
              '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
              '$(SDKROOT)/System/Library/Frameworks/IOKit.framework',
              '$(SDKROOT)/usr/lib/libbsm.dylib',
            ],
          },
        }, { # else: OS!=mac
          'sources!': [ 'misc/capture_context_mac.S' ],
        }],
        ['OS=="win"', {
          'link_settings': {
            'libraries': [
              '-luser32.lib',
              '-lversion.lib',
              '-lwinhttp.lib',
            ],
          },
          'msvs_disabled_warnings': [
            4201,  # nonstandard extension used : nameless struct/union.
            4577,  # 'noexcept' used with no exception handling mode specified
          ],
          'direct_dependent_settings': {
            'msvs_disabled_warnings': [
              4577,  # 'noexcept' used with no exception handling mode specified
            ],
          },
          'conditions': [
            ['target_arch=="ia32"', {
              'msvs_settings': {
                'MASM': {
                  'UseSafeExceptionHandlers': 'true',
                },
              },
            }],
          ],
        }, {  # else: OS!="win"
          'sources!': [
            'misc/capture_context_win.asm',
            'win/safe_terminate_process.asm',
          ],
        }],
        ['OS=="android"', {
          'link_settings': {
            'libraries': [
              '-llog',
            ],
          },
        }],
        ['OS=="linux" or OS=="android"', {
          'sources': [
            'net/http_transport_socket.cc',
            'process/process_memory_sanitized.cc',
            'process/process_memory_sanitized.h',
          ],
        }, {  # else: OS!="linux"
          'sources!': [
            'misc/capture_context_linux.S',
          ],
        }],
        ['OS!="linux" and OS!="android"', {
          'sources/': [
            ['exclude', '^process/'],
          ],
        }],
      ],
      'target_conditions': [
        ['OS=="android"', {
          'sources/': [
            ['include', '^linux/'],
            ['include', '^misc/capture_context_linux\\.S$'],
            ['include', '^misc/paths_linux\\.cc$'],
            ['include', '^misc/time_linux\\.cc$'],
            ['include', '^posix/process_info_linux\\.cc$'],
            ['include', '^process/process_memory_linux\\.cc$'],
            ['include', '^process/process_memory_linux\\.h$'],
          ],
        }, { # else: OS!="android"
          'sources!': [
            'stream/log_output_stream.cc',
            'stream/log_output_stream.h',
          ]
        }],
      ],
    },
  ],
}
