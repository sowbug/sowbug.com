+++
date = "2004-03-13T11:12:54+00:00"
title = "23 Prisoners, in code"
+++

\--- title: 23 Prisoners, in code mt_id: 38 layout: post date: 2004-03-13
11:12:54 +00:00 \--- And here is a C program that tests my solution. `

    
    
    #include <stdlib.h>  
    #include <stdio.h>  
      
    #define PRISONERS_COUNT (23)  
    #define STRAGGLER_FACTOR (4)  
      
    enum {  
      MANAGER_SYNC,  
      MANAGER_RESYNC,  
      MANAGER_COUNT,  
      PRISONER_UNKNOWN,  
      PRISONER_UNKNOWN_SAW_ON,  
      PRISONER_UNKNOWN_SAW_OFF,  
      PRISONER_READY,  
      PRISONER_IDLE  
    };  
      
    enum {  
      ACTION_UNDECIDED,  
      ACTION_FLIP_A,  
      ACTION_FLIP_B,  
      ACTION_CALL_WARDEN  
    };  
      
    int switch_a, switch_b;  
    int prisoner_visited[PRISONERS_COUNT];  
    int prisoner_state[PRISONERS_COUNT];  
    int manager_count;  
    int manager_straggler_count;  
    int stats_visits;  
      
    static int call_warden(void) {  
      int i = PRISONERS_COUNT;  
      while (i--) {  
        if (0 == prisoner_visited[i]) {  
          return 1; // execute  
        }  
      }  
      return 0; // set free  
    }  
      
    static int visit_room(int prisoner) {  
      int action = ACTION_UNDECIDED;  
      
      prisoner_visited[prisoner]++;  
      
      switch (prisoner_state[prisoner]) {  
      case MANAGER_SYNC:  
        action = ACTION_FLIP_A;  
        if (switch_a) {  
          prisoner_state[prisoner] = MANAGER_COUNT;  
        }  
        break;  
      case MANAGER_RESYNC:  
        if (switch_a) {  
          if (++manager_count == PRISONERS_COUNT) {  
            action = ACTION_CALL_WARDEN;  
          } else {  
            action = ACTION_FLIP_A;  
          }  
        } else {  
          action = ACTION_FLIP_A;  
          prisoner_state[prisoner] = MANAGER_SYNC;  
        }  
        break;  
      case MANAGER_COUNT:  
        if (switch_a) {  
          if (++manager_count == PRISONERS_COUNT) {  
            action = ACTION_CALL_WARDEN;  
          } else {  
            action = ACTION_FLIP_A;  
          }  
        } else {  
          action = ACTION_FLIP_B;  
          if (++manager_straggler_count > STRAGGLER_FACTOR) {  
            manager_straggler_count = 0;  
            prisoner_state[prisoner] = MANAGER_RESYNC;  
          }  
        }  
        break;  
      case PRISONER_UNKNOWN:  
        action = ACTION_FLIP_B;  
        if (switch_a) {  
          prisoner_state[prisoner] = PRISONER_UNKNOWN_SAW_ON;  
        } else {  
          prisoner_state[prisoner] = PRISONER_UNKNOWN_SAW_OFF;  
        }  
        break;  
      case PRISONER_UNKNOWN_SAW_ON:  
        action = ACTION_FLIP_B;  
        if (!switch_a) {  
          prisoner_state[prisoner] = PRISONER_READY;  
        }  
        break;  
      case PRISONER_UNKNOWN_SAW_OFF:  
        action = ACTION_FLIP_B;  
        if (switch_a) {  
          prisoner_state[prisoner] = PRISONER_READY;  
        }  
        break;  
      case PRISONER_READY:  
        if (!switch_a) {  
          action = ACTION_FLIP_A;  
          prisoner_state[prisoner] = PRISONER_IDLE;  
        } else {  
          action = ACTION_FLIP_B;  
        }  
        break;  
      case PRISONER_IDLE:  
        action = ACTION_FLIP_B;  
        break;  
      }  
      
      switch (action) {  
        case ACTION_FLIP_A:  
          switch_a = !switch_a;  
          break;  
        case ACTION_FLIP_B:  
          switch_b = !switch_b;  
          break;  
        case ACTION_CALL_WARDEN:  
          return 1;  
        default:  
          printf("ERROR: no action taken by prisoner #%d\n", prisoner);  
          return -1;  
      }  
      return 0;  
    }  
      
    static int run_session(void) {  
      int i;  
      
      for (i = 0; i < PRISONERS_COUNT; i++) {  
        prisoner_state[i] = PRISONER_UNKNOWN;  
        prisoner_visited[i] = 0;  
      }  
      prisoner_state[0] = MANAGER_SYNC;  
      manager_count = 1; // always count self  
      manager_straggler_count = 0;  
      switch_a = abs(rand()) % 2;  
      switch_b = abs(rand()) % 2;  
      stats_visits = 0;  
      
      while (1) {  
        int r = visit_room(abs(rand()) % PRISONERS_COUNT);  
        stats_visits++;  
        if (1 == r) {  
          return call_warden();  
        }  
        if (-1 == r) {  
          return 1; // same as dying  
        }  
      }  
    }  
      
    int main(int argc, char* argv[]) {  
      int i = 0;  
      int visits_total = 0;  
      
      while (i++ < 5000) {  
        printf(".");  
        if (1 == run_session()) {  
          printf("executed after %d visits.\n", stats_visits);  
          break;  
        }  
        visits_total += stats_visits;  
      }  
      printf("Average visits per session: %d (%d/prisoner)\n", visits_total / i,  
        (visits_total / i) / PRISONERS_COUNT);  
      return 0;  
    }  
      
    

`

