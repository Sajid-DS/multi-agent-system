## Multi Agent System

A modular, collaborative AI system where specialized agents work together to research topics, analyze information, and generate structured summaries. This system demonstrates modern agent orchestration patterns using LangChain for agent management and a custom message bus for inter-agent communication.


## Workflow 

┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                      │
└─────────────────────────────┬───────────────────────────────┘
                              │ (Topic Query)
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Orchestrator Layer                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                     Orchestrator                      │  │
│  │  • Coordinates workflow                              │  │
│  │  • Manages agent dependencies                        │  │
│  │  • Handles error recovery                            │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────┬─────────────┬─────────────────────────┘
                      │             │
           (Research Request)  (Results Forwarding)
                      │             │
                      ▼             ▼
┌─────────────────────────────────────────────────────────────┐
│                    Agent Layer                               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │  Research   │  │  Analysis   │  │  Summary    │       │
│  │   Agent     │◄─┤   Agent     │◄─┤   Agent     │       │
│  │             │  │             │  │             │       │
│  └──────┬──────┘  └─────────────┘  └─────────────┘       │
│         │                                                 │
│         ▼                                                 │
│  ┌─────────────┐                                         │
│  │ Web Search  │                                         │
│  │   Tools     │                                         │
│  └─────────────┘                                         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Communication Layer                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    Message Bus                       │  │
│  │  • Pub/Sub messaging                                │  │
│  │  • Asynchronous communication                        │  │
│  │  • Message persistence                              │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
