using UnityEngine;
using UnityEngine.SceneManagement;

public class ApartmentGame : MonoBehaviour
{
    public float timeLimit = 180f;
    public Transform player;
    public Transform securityBot;
    public Transform exit;
    public Transform[] keys;
    public int health = 100;
    private float timeLeft;
    private int collected;
    private Vector3 botStart;
    private bool finished;

    void Start(){ timeLeft=timeLimit; if(securityBot) botStart=securityBot.position; }
    void Update(){
        if(finished) return;
        timeLeft-=Time.deltaTime;
        if(timeLeft<=0){ timeLeft=0; finished=true; Debug.Log("GAME OVER: Time up"); }
        for(int i=0;i<keys.Length;i++) if(keys[i] && Vector3.Distance(player.position,keys[i].position)<1.4f){ keys[i].gameObject.SetActive(false); keys[i]=null; collected++; }
        if(securityBot){
            Vector3 p=securityBot.position;
            p.x=botStart.x+Mathf.Sin(Time.time*1.5f)*3f;
            securityBot.position=p;
            if(Vector3.Distance(player.position,securityBot.position)<1.25f && Time.frameCount%45==0){ health-=20; if(health<=0){finished=true;Debug.Log("GAME OVER: Security bot");} }
        }
        if(collected>=3 && Vector3.Distance(player.position,exit.position)<2f){finished=true;Debug.Log("YOU ESCAPED!");}
    }
    public int KeysCollected()=>collected;
    public float TimeLeft()=>timeLeft;
    public void Restart(){SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);}
}
