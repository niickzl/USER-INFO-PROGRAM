Background:
YouTube rate limited Discord bots from streaming audio, causing many popular music bots to shut down.
As a fun challenge, I attempted to create a private music bot.

Features:
Responds to "@zlbot" or "!!!" commands
Simple Commands include: join, leave, play, skip, and help
Streams YouTube audio when given a YouTube link
Implements a song queue system for continuous playback
 
The bot works by:
Downloading audio as an Opus file (instead of streaming directly from YouTube)
Streaming the downloaded file
Deleting the file after playback

​Development Journey:
Initial attempts at direct streaming were limited by YouTube
Explored alternative music APIs (SoundCloud, Spotify, Amazon Music, Deezer) which failed
Discovered a solution by downloading rather than streaming from YouTube's API
Found an issue where if a song was terminated before finishing, its audio file will not be deleted
Tried resolving by:
Delaying execution (time.sleep(1-10s))
Terminating specific FFmpeg processes via a dictionary [PATH: process](Code remained in the file)
Both were unsuccessful and failed file deletion after termination remains an ongoing issue.
