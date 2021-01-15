using System.Threading;
using NAudio.Wave;

namespace solving_exercises
{
    class Program
    {
        static void Main(string[] args)
        {
            IWavePlayer waveOutDevice = new WaveOut();
            AudioFileReader audioFileReader = new AudioFileReader(@"C:\021.mp3");

            waveOutDevice.Init(audioFileReader);
            waveOutDevice.Play();
            while (waveOutDevice.PlaybackState == PlaybackState.Playing)
            {
               Thread.Sleep(100);
            }
        }
    }
}
