# Changelog

All notable changes to this project will be documented in this file.

This project uses semantic versioning.

## 0.0.8

### Added

- Added public installation documentation for Codex/OpenAI, Claude Code, generic agents, agent-assisted installation, and troubleshooting.
- Added packaging strategy documentation for repository, Skill target, and adapter package boundaries.
- Added compatibility matrix covering Skill folder support, persistent instruction files, Review Subagent Loop support, fallbacks, and best use cases.
- Added lightweight usage examples for Next.js, FastAPI, and Laravel projects.
- Updated the README with installation, compatibility, usage, and example links while keeping it in draft form.

## 0.0.7

### Added

- Added Goal Completion Mode so a user-provided objective becomes the active goal without requiring a universal `/goal` command.
- Added persistent project memory guidance for project control files and continuation-safe state.
- Added continuation and cross-session handoff protocol with latest reliable state priority and final status criteria.
- Updated Skill references and templates to capture active objective, goal mode, handoff summary, resume instructions, blockers, and review status.

## 0.0.6

### Added

- Added the objective intake questionnaire, intake modes, and ask-only-blocking-questions policy.
- Added the autonomous run kickoff protocol with Objective Brief, kickoff response, and continuation kickoff formats.
- Clarified assumption handling, default A3 autonomy, and A4 usage only for explicitly requested continuous autonomous loops.
- Updated project control templates to capture Objective Brief, definition of done, validation plan, review plan, and continuation context.

## 0.0.5

### Added

- Added detailed autonomy levels from A0 manual mode through A4 continuous autonomous loop.
- Added the Review Subagent Loop with real-subagent primary mode and independent-review fallback mode.
- Added reviewer roles, scoring policy, review round limits, and review-driven stop conditions.
- Expanded safety gates and approval policies for critical dependencies, licensing, tests, and validation tooling.
- Updated final report and project control templates to capture review rounds, scores, required fixes, deferred suggestions, and final review status.

## 0.0.4

### Added

- Added stack detection and command discovery playbooks for frontend, backend, mobile, and infrastructure projects.
- Added command discovery guidance for project-defined commands, package manager detection, safe command selection, and validation reporting.
- Expanded stack detection signals across JavaScript/TypeScript, Python, PHP, Ruby, Java/JVM, .NET, Go, Rust, mobile, and infra/DevOps projects.
- Documented Step 4 stack detection and command discovery decisions.

## 0.0.3

### Added

- Added reusable project control file templates to both Skill asset directories.
- Added templates for agent instructions, Claude instructions, backlog, roadmap, development log, test plan, decisions, known issues, active ToDos, and final reports.
- Documented the Step 3 project control template strategy.
- Updated Skill references to explain when to create, suggest, or adapt control file templates.

## 0.0.2

### Added

- Defined the Step 2 internal Skill architecture and core autonomous development loop behavior.
- Replaced initial Skill placeholders with concise behavior entry points for Codex/OpenAI and Claude Code.
- Added mirrored Skill reference files for objective intake, autonomy, loop protocol, ToDos, scope management, safety gates, stack detection, testing, repair, documentation, and final reports.

## 0.0.1

### Added

- Initialized the project planning foundation.
- Documented the project purpose, audience, compatibility goals, autonomy model, scope, and stack strategy.
- Documented the Step 1 repository structure and installation strategy.
- Added initial Codex/OpenAI and Claude Code Skill placeholder folders.
- Added installation notes for Codex/OpenAI, Claude Code, and generic agents.
- Added reusable adapter templates for `AGENTS.md`, `CLAUDE.md`, and generic AI coding agents.
- Added initial contribution and repository agent instruction files.
- Added reserved example folders for future Next.js, FastAPI, and Laravel examples.
- Added the initial public README draft.
- Added the MIT License.
