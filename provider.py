import asyncio
import time

class Provider:
    def __init__(self, name, rate_limit_per_window, window_duration):
        self.name = name
        self.rate_limit_per_window = rate_limit_per_window
        self.window_duration = window_duration  # in seconds
        self.queue = asyncio.Queue()  # Queue for storing incoming requests
        self.last_processed_time = 0  # Last time requests were processed
        self.total_sent_requests = 0  # Total number of requests sent
        self.total_pending_requests = 0  # Total number of requests in queue

    async def process_requests(self):
        while True:
            current_time = time.time()
            if current_time - self.last_processed_time >= self.window_duration:
                batch_size = min(self.rate_limit_per_window, self.queue.qsize())
                if batch_size > 0:
                    print(f"Provider {self.name}: Processing a batch of {batch_size} requests.")
                for _ in range(batch_size):
                    request = await self.queue.get()
                    self._send_request(request)
                    self.total_sent_requests += 1
                self.last_processed_time = current_time
            await asyncio.sleep(1)  # Sleep for a second to avoid busy-waiting

    def _send_request(self, request):
        print(f"Sending request: {request} to provider {self.name}")

    async def add_request(self):
        await self.queue.put("New Request")
        self.total_pending_requests += 1
        print(f"Request added to {self.name}'s queue. Pending requests: {self.total_pending_requests}")

    def get_status(self):
        return {
            "sent_requests": self.total_sent_requests,
            "pending_requests": self.total_pending_requests,
        }