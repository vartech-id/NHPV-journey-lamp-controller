import { ref } from "vue";

export function useCountdown(initialSeconds = 10) {
  const countdown = ref(initialSeconds);

  const reset = (seconds = initialSeconds) => {
    countdown.value = seconds;
  };

  const start = (onDone) => {
    setTimeout(async () => {
      if (countdown.value > 0) {
        countdown.value -= 1;
        start(onDone);
      } else {
        try {
          if (typeof onDone === "function") {
            await onDone();
          }
        } catch (e) {
          console.error("onDone error:", e);
        }
      }
    }, 1000);
  };
  
  return { countdown, start, reset };
}
