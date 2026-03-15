# Prompt Files Index (`prompts/`)

Indexed list of prompt files in `/a0/prompts` and their purpose.

1. `agent.context.extras.md` - Injects extra runtime context into the main prompt assembly.
2. `agent.extras.agent_info.md` - Provides static metadata about the current agent/profile.
3. `agent.extras.workdir_structure.md` - Describes working-directory layout and file organization context.
4. `agent.system.behaviour.md` - Primary behavior-policy prompt fragment for the agent.
5. `agent.system.behaviour_default.md` - Fallback/default behavior profile when custom behavior is absent.
6. `agent.system.datetime.md` - Injects current date/time and temporal handling guidance.
7. `agent.system.main.communication.md` - Defines response style and communication constraints.
8. `agent.system.main.communication_additions.md` - Adds extra communication rules layered onto base communication prompt.
9. `agent.system.main.environment.md` - Describes environment/tooling assumptions available to the agent.
10. `agent.system.main.md` - Top-level system prompt scaffold for the core agent.
11. `agent.system.main.role.md` - Defines agent identity, role, and expected stance.
12. `agent.system.main.solving.md` - Sets default problem-solving strategy and execution behavior.
13. `agent.system.main.tips.md` - Contains curated operational tips injected into system prompt.
14. `agent.system.main.tips.py` - Python helper that composes/generates dynamic tips prompt content.
15. `agent.system.mcp_tools.md` - Defines MCP/tools usage policy and available tool behavior.
16. `agent.system.memories.md` - Adds memory-system operating instructions to the system prompt.
17. `agent.system.projects.active.md` - Context rules for currently active project handling.
18. `agent.system.projects.inactive.md` - Context rules for inactive/archived project handling.
19. `agent.system.projects.main.md` - Project-awareness orchestration prompt for active/inactive projects.
20. `agent.system.response_tool_tips.md` - Hints for using response-formatting/tooling in final outputs.
21. `agent.system.secrets.md` - Security guidance for handling secrets/sensitive information.
22. `agent.system.skills.loaded.md` - Injected list/metadata of currently loaded skills.
23. `agent.system.skills.md` - Core instructions for skill discovery and usage.
24. `agent.system.solutions.md` - Rules for solution tracking/retrieval behavior.
25. `agent.system.tool.a2a_chat.md` - Instructions for agent-to-agent chat tool usage.
26. `agent.system.tool.behaviour.md` - Instructions for behavior management tool usage.
27. `agent.system.tool.browser.md` - Instructions for browser/web-navigation tool usage.
28. `agent.system.tool.call_sub.md` - Instructions for spawning/calling subordinate agents.
29. `agent.system.tool.call_sub.py` - Python helper for subordinate-agent tool prompt assembly.
30. `agent.system.tool.code_exe.md` - Instructions for execute-code/runtime tool usage.
31. `agent.system.tool.document_query.md` - Instructions for document-query/retrieval tool usage.
32. `agent.system.tool.input.md` - Instructions for user-input/request-input tool behavior.
33. `agent.system.tool.memory.md` - Instructions for memory read/write/query tool behavior.
34. `agent.system.tool.notify_user.md` - Instructions for user-notification tool usage.
35. `agent.system.tool.response.md` - Instructions for structured response/finalization tool usage.
36. `agent.system.tool.scheduler.md` - Instructions for scheduler/time-based task tool usage.
37. `agent.system.tool.search_engine.md` - Instructions for search engine/query tool usage.
38. `agent.system.tool.skills.md` - Instructions for skills-management tool usage.
39. `agent.system.tool.wait.md` - Instructions for wait/polling tool usage.
40. `agent.system.tools.md` - Aggregate tools prompt that references specific tool prompt fragments.
41. `agent.system.tools.py` - Python helper that assembles tool prompt content dynamically.
42. `agent.system.tools_vision.md` - Tool-use guidance specific to vision/image capabilities.
43. `behaviour.merge.msg.md` - User/message template used during behavior-merge operations.
44. `behaviour.merge.sys.md` - System prompt for combining behavior definitions.
45. `behaviour.search.sys.md` - System prompt for behavior lookup/search process.
46. `behaviour.updated.md` - Output/notification template indicating behavior update completion.
47. `browser_agent.system.md` - Standalone system prompt for the browser-specialized agent.
48. `fw.ai_response.md` - Framework template for normal AI response envelope.
49. `fw.bulk_summary.msg.md` - Message template for bulk-summary requests.
50. `fw.bulk_summary.sys.md` - System prompt for generating bulk summaries.
51. `fw.code.info.md` - Informational framework message for code execution state.
52. `fw.code.max_time.md` - Framework message when code execution exceeds max allowed time.
53. `fw.code.no_out_time.md` - Framework message for no-output over time condition.
54. `fw.code.no_output.md` - Framework message when code execution returns no output.
55. `fw.code.pause_dialog.md` - Framework prompt/dialog for paused code execution.
56. `fw.code.pause_time.md` - Framework message when execution is paused due to duration.
57. `fw.code.reset.md` - Framework message for code runtime reset event.
58. `fw.code.running.md` - Framework status message indicating code is running.
59. `fw.code.runtime_wrong.md` - Framework error template for wrong/invalid runtime selection.
60. `fw.document_query.optmimize_query.md` - Framework prompt for query optimization in document retrieval (filename has typo: `optmimize`).
61. `fw.document_query.system_prompt.md` - System prompt used by framework document-query flow.
62. `fw.error.md` - Generic framework error message template.
63. `fw.hint.call_sub.md` - Hint template nudging use of subordinate-agent calls.
64. `fw.initial_message.md` - Initial framework message template shown at session start.
65. `fw.intervention.md` - Framework intervention/override message template.
66. `fw.knowledge_tool.response.md` - Response template for knowledge-tool outputs.
67. `fw.memories_deleted.md` - Framework confirmation message for memory deletion actions.
68. `fw.memories_not_found.md` - Framework message when requested memories are missing.
69. `fw.memory.hist_suc.sys.md` - System prompt for successful memory history summarization/retrieval.
70. `fw.memory.hist_sum.sys.md` - System prompt for memory history summary generation.
71. `fw.memory_saved.md` - Framework confirmation template after memory save.
72. `fw.msg_cleanup.md` - Framework message for cleanup/housekeeping notices.
73. `fw.msg_critical_error.md` - Framework message for critical error reporting.
74. `fw.msg_from_subordinate.md` - Framework wrapper for messages coming from subordinate agents.
75. `fw.msg_misformat.md` - Framework message for malformed/invalid user or tool message format.
76. `fw.msg_nudge.md` - Framework nudge/reminder message template.
77. `fw.msg_repeat.md` - Framework prompt to handle repeated user messages/loops.
78. `fw.msg_summary.md` - Framework message template for concise summaries.
79. `fw.msg_timeout.md` - Framework timeout notification template.
80. `fw.msg_truncated.md` - Framework notification for truncated content/messages.
81. `fw.notify_user.notification_sent.md` - Framework confirmation that a user notification was sent.
82. `fw.rename_chat.msg.md` - Message template for chat-title rename operations.
83. `fw.rename_chat.sys.md` - System prompt for generating/choosing chat renames.
84. `fw.tool_not_found.md` - Framework error template when requested tool is unavailable.
85. `fw.tool_result.md` - Framework wrapper template for presenting tool results.
86. `fw.topic_summary.msg.md` - Message template for topic-summary outputs.
87. `fw.topic_summary.sys.md` - System prompt for creating topic summaries.
88. `fw.user_message.md` - Framework template that wraps/processes incoming user messages.
89. `fw.wait_complete.md` - Framework message indicating wait operation completed.
90. `fw.warning.md` - Generic framework warning message template.
91. `memory.consolidation.msg.md` - Message template used for memory consolidation pipeline.
92. `memory.consolidation.sys.md` - System prompt for consolidating related memories.
93. `memory.keyword_extraction.msg.md` - Message template for keyword extraction tasks in memory flow.
94. `memory.keyword_extraction.sys.md` - System prompt for extracting keywords from content.
95. `memory.memories_filter.msg.md` - Message template for memory filtering stage.
96. `memory.memories_filter.sys.md` - System prompt for selecting/filtering relevant memories.
97. `memory.memories_query.msg.md` - Message template for memory query requests/results.
98. `memory.memories_query.sys.md` - System prompt for querying memory store.
99. `memory.memories_sum.sys.md` - System prompt for summarizing retrieved memories.
100. `memory.recall_delay_msg.md` - Message template shown when memory recall is delayed.
101. `memory.solutions_query.sys.md` - System prompt for querying stored solutions.
102. `memory.solutions_sum.sys.md` - System prompt for summarizing stored solutions.
