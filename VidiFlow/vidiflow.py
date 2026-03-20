import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
import yt_dlp

# Professional UI Styling
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class VidiFlow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("VidiFlow - Universal Media Grabber")
        self.geometry("620x500")
        
        self.save_path = os.path.join(os.path.expanduser("~"), "Downloads")
        self.media_info = None

        # --- UI Elements ---
        self.header = ctk.CTkLabel(self, text="VidiFlow", font=("Segoe UI", 32, "bold"), text_color="#3b8ed0")
        self.header.pack(pady=(30, 5))

        self.tagline = ctk.CTkLabel(self, text="Clean. Fast. Universal.", font=("Segoe UI", 13), text_color="gray")
        self.tagline.pack(pady=(0, 20))

        self.url_entry = ctk.CTkEntry(self, width=520, height=45, placeholder_text="Paste Video or Reel Link (YouTube, FB, Insta...)")
        self.url_entry.pack(pady=10)

        self.fetch_btn = ctk.CTkButton(self, text="Analyze Link", height=35, command=self.fetch_video_data)
        self.fetch_btn.pack(pady=10)

        self.status_box = ctk.CTkFrame(self, fg_color="transparent")
        self.status_box.pack(pady=10)
        
        self.status_label = ctk.CTkLabel(self.status_box, text="Ready to flow...", font=("Segoe UI", 12))
        self.status_label.pack()

        self.quality_dropdown = ctk.CTkOptionMenu(self, width=400, values=["1. Paste link & Analyze"])
        self.quality_dropdown.pack(pady=15)

        self.download_btn = ctk.CTkButton(self, text="Start Download", state="disabled", fg_color="#2ecc71", hover_color="#27ae60", height=45, font=("Segoe UI", 16, "bold"), command=self.run_download)
        self.download_btn.pack(pady=20)

        self.footer = ctk.CTkLabel(self, text=f"Target: {self.save_path}", font=("Segoe UI", 10), text_color="gray")
        self.footer.pack(side="bottom", pady=10)

    def fetch_video_data(self):
        url = self.url_entry.get().strip()
        if not url:
            return messagebox.showwarning("Empty Link", "Please provide a valid URL.")

        self.status_label.configure(text="🔍 Searching for media...", text_color="orange")
        self.update()

        try:
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                self.media_info = ydl.extract_info(url, download=False)
                
                # Setup options
                formats = [
                    "Best Video + Audio (MP4)",
                    "High Quality Audio Only (MP3)"
                ]
                
                self.quality_dropdown.configure(values=formats)
                self.quality_dropdown.set(formats[0])
                
                title = self.media_info.get('title', 'Video Found')
                self.status_label.configure(text=f"✅ Found: {title[:45]}...", text_color="#2ecc71")
                self.download_btn.configure(state="normal")

        except Exception as e:
            self.status_label.configure(text="❌ Link not supported or private.", text_color="#e74c3c")
            messagebox.showerror("Error", "Could not fetch media. Check the link or your internet.")

    def run_download(self):
        url = self.url_entry.get()
        choice = self.quality_menu_logic()
        
        opts = {
            'format': choice['fmt'],
            'outtmpl': os.path.join(self.save_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }

        if choice['is_audio']:
            opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]

        try:
            self.download_btn.configure(text="Downloading...", state="disabled")
            self.status_label.configure(text="⚡ Streaming data to disk...", text_color="#3b8ed0")
            self.update()
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
            
            messagebox.showinfo("Success", "Download Complete! Check your folder.")
            self.status_label.configure(text="Ready to flow...", text_color="gray")
        except Exception as e:
            messagebox.showerror("Download Failed", str(e))
        finally:
            self.download_btn.configure(text="Start Download", state="normal")

    def quality_menu_logic(self):
        selection = self.quality_dropdown.get()
        if "Audio" in selection:
            return {"fmt": "bestaudio/best", "is_audio": True}
        return {"fmt": "bestvideo+bestaudio/best", "is_audio": False}

if __name__ == "__main__":
    app = VidiFlow()
    app.mainloop()
