# Mobile Playbooks

Use this reference for mobile objectives after reading `stack-detection.md` and `command-discovery.md`.

## General Mobile Flow

1. Identify platform: React Native, Expo, Flutter, native Android, native iOS, or hybrid.
2. Inspect package scripts or platform config.
3. Prefer static checks and tests before heavy builds.
4. Avoid signing, store upload, deployment, or device-management commands without explicit authorization.

## React Native

Signals:

- `react-native.config.js`
- `android/`
- `ios/`
- React Native dependencies in `package.json`

Likely validation:

- package script for `lint`
- package script for `typecheck`
- package script for `test`
- package script for platform build only when relevant

Prefer project scripts over raw platform commands.

## Expo

Signals:

- `expo.*`
- `app.json`
- Expo dependencies

Likely validation:

- package script for `lint`
- package script for `typecheck`
- package script for `test`
- Expo checks if documented by the project

Do not publish, submit, or update builds without explicit authorization.

## Flutter

Signals:

- `pubspec.yaml`
- `android/`
- `ios/`

Likely validation:

- `flutter analyze`
- `flutter test`
- `flutter build` only when appropriate and not too heavy

Avoid signing or release build commands unless explicitly authorized.

## Kotlin Android

Signals:

- `android/`
- `build.gradle`
- `settings.gradle`
- `gradlew`

Likely validation:

- Gradle test tasks
- Gradle lint tasks
- Debug build tasks when relevant

Prefer `./gradlew` wrapper when present.

## Swift iOS

Signals:

- `ios/`
- `.xcodeproj`
- `.xcworkspace`
- Swift files

Likely validation:

- documented project commands
- test schemes when discoverable
- build checks only when environment supports them

If local tooling is unavailable, document the limitation.

## Mobile Reporting

Report whether validation covered:

- JavaScript/TypeScript layer
- Native layer
- Shared business logic
- Platform build
- Manual/device validation

Do not claim device validation unless it actually happened.
